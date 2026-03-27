# 🌍 Global Health Dashboard

An interactive web dashboard built with **Flask** and **pandas** to explore global health trends across 167 countries from 2014 to 2022.

Live demo: [hakansahin.dev](https://hakansahin.dev)

---

## Features

- **Overview cards** — total countries, year range, average life expectancy and health expenditure
- **Life expectancy trend** — year-by-year line chart for any selected country
- **Top 10 countries** — ranked bar chart by life expectancy, health expenditure, or infant mortality
- **Health expenditure vs life expectancy** — scatter plot showing correlation across all countries
- **Country detail table** — full year-by-year breakdown per country including HIV prevalence and infant mortality

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python · Flask |
| Data processing | pandas · numpy |
| Frontend | HTML · CSS · JavaScript |
| Charts | Chart.js |
| Data source | Kaggle — Global Health Statistics |

---

## Project Structure

```
Pandas_project/
├── app.py               # Flask backend & API endpoints
├── data/
│   └── Global_Health.csv
├── templates/
│   └── index.html       # Dashboard UI
└── static/
    └── charts.js
```

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Main dashboard |
| `GET /api/overview` | Global summary stats |
| `GET /api/life_expect_trend?country=X` | Life expectancy trend for a country |
| `GET /api/top_countries?metric=X&year=Y` | Top 10 countries by metric |
| `GET /api/scatter?year=Y` | Health exp vs life expectancy scatter data |
| `GET /api/country_detail?country=X` | Full year-by-year data for a country |

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/Elcebir71/global-health-dashboard.git
cd global-health-dashboard

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install flask pandas

# Run
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## Data

Dataset: [Global Health Statistics](https://www.kaggle.com/datasets/malaiarasugraj/global-health-statistics) via Kaggle.

Key columns: `life_expect`, `health_exp`, `infant_mortality`, `under_5_mortality`, `prev_hiv`, `inci_tuberc`, `prev_undernourishment`

---

## Author

**Hakan Şahin** — [hakansahin.dev](https://hakansahin.dev) · [GitHub](https://github.com/Elcebir71) · [LinkedIn](https://linkedin.com/in/hakan-sahin)
