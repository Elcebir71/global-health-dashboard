import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

df = pd.read_csv("data/Global_Health.csv")
df.columns = df.columns.str.strip()
LAST_YEAR = int(df[df["life_expect"].notna()]["Year"].max())
years = sorted(df[df["Year"] <= LAST_YEAR]["Year"].unique().tolist())

@app.route("/")
def index():
    countries = sorted(df["Country"].unique().tolist())
    return render_template("index.html", countries=countries, years=years, last_year=LAST_YEAR) 

@app.route("/api/overview")
def overview():
    latest = df[df["Year"] == LAST_YEAR]
    return jsonify({
        "total_countries": int(df["Country"].nunique()),
        "year_range": f"{int(df['Year'].min())} - {LAST_YEAR}",
        "avg_life_expect": round(float(latest["life_expect"].dropna().mean()), 1),
        "avg_health_exp": round(float(latest["health_exp"].dropna().mean()), 1),
    })

@app.route("/api/life_expect_trend")
def life_expect_trend():
    country = request.args.get("country", "Netherlands")
    data = df[df["Country"] == country][["Year", "life_expect"]].dropna()
    return jsonify(data.to_dict(orient="records"))

@app.route("/api/top_countries")
def top_countries():
    metric = request.args.get("metric", "life_expect")
    year = int(request.args.get("year", LAST_YEAR))
    data = (df[df["Year"] == year][["Country", metric]]
            .dropna()
            .sort_values(metric, ascending=False)
            .head(10))
    return jsonify(data.to_dict(orient="records"))

@app.route("/api/scatter")
def scatter():
    year = int(request.args.get("year", LAST_YEAR))
    data = df[df["Year"] == year][["Country", "health_exp", "life_expect"]].dropna()
    return jsonify(data.to_dict(orient="records"))

@app.route("/api/country_detail")
def country_detail():
    country = request.args.get("country", "Netherlands")
    data = df[(df["Country"] == country) & (df["Year"] <= LAST_YEAR)].sort_values("Year")
    cols = ["Year", "life_expect", "health_exp", "infant_mortality",
            "under_5_mortality", "prev_hiv", "inci_tuberc"]
    return jsonify(data[cols].fillna("N/A").to_dict(orient="records"))

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)