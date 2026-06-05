# Polyhouse Sensor Project

## Objective

This project processes polyhouse sensor data, performs data cleaning, and conducts exploratory data analysis (EDA) to understand relationships between environmental conditions and crop yield.

---

## Project Structure

```
polyhouse-sensor-project/
│
├── data/
│   ├── raw/
│   │   ├── climate_data.csv
│   │   ├── polyhouse_sensor.csv
│   │   └── yield_data.csv
│   │
│   └── processed/
│       ├── 01_combined.csv
│       ├── 02_cleaned.parquet
│       └── sample_cleaned_data.csv
│
├── docs/
│   └── cleaning_log.md
│
├── reports/
│   ├── data_quality.md
│   ├── eda_summary.md
│   └── figures/
│       ├── correlation_heatmap.png
│       ├── humidity_vs_yield.png
│       ├── co2_vs_yield.png
│       └── temperature_vs_yield.png
│
├── src/
│   ├── ingest_data.py
│   ├── clean_data.py
│   └── eda.py
│
└── README.md
```

---

## Features

### Task 2 – Data Cleaning

- Loads raw sensor, climate, and yield datasets.
- Audits missing values.
- Cleans and preprocesses data.
- Generates cleaned dataset in Parquet format.
- Produces sample cleaned dataset.
- Documents all cleaning decisions.

### Task 3 – Exploratory Data Analysis (EDA)

- Generates descriptive statistics.
- Produces data quality report.
- Creates correlation heatmap.
- Creates scatter plots for:
  - Humidity vs Yield
  - CO₂ vs Yield
  - Temperature vs Yield
- Documents insights from environmental variables and crop yield.

---

## Data Cleaning Strategy

- Temperature: Missing values imputed using median.
- Humidity: Missing values imputed using median.
- CO₂: Missing values imputed using median.
- Yield: Rows with missing target values removed.

Cleaning rationale is documented in:

```
docs/cleaning_log.md
```

---

## Data Quality Summary

| Metric | Value |
|----------|----------|
| Total Observations | 50 |
| Date Range | 2026-06-01 to 2026-06-05 |
| Mean Temperature | 29.92 °C |
| Mean Humidity | 62.72 % |
| Mean CO₂ | 440.90 ppm |
| Mean Yield | 124.00 kg |

---

## Key EDA Insights

### Humidity and Yield

Humidity values range from 57% to 69%. Yield remains relatively stable across this range, indicating a moderate relationship between humidity and crop yield.

### CO₂ and Yield

Higher CO₂ levels generally correspond to slightly higher yield values, suggesting that increased CO₂ concentration may support plant growth inside the polyhouse environment.

### Temperature and Yield

Temperature remains within a narrow range (26.5°C–32.4°C). Yield variation is limited, indicating relatively stable growing conditions.

### Correlation Notes

- Correlation heatmap was generated to identify relationships among variables.
- Correlation does not imply causation.
- The dataset contains only 50 observations, so conclusions should be interpreted carefully.

---

## Output Files

### Cleaned Dataset

```
data/processed/02_cleaned.parquet
```

### Sample Dataset

```
data/processed/sample_cleaned_data.csv
```

### Cleaning Log

```
docs/cleaning_log.md
```

### Data Quality Report

```
reports/data_quality.md
```

### EDA Summary

```
reports/eda_summary.md
```

### Figures

```
reports/figures/
```

---

## How to Run

### Data Ingestion

```bash
python src/ingest_data.py
```

### Data Cleaning

```bash
python src/clean_data.py
```

### Exploratory Data Analysis

```bash
python src/eda.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Parquet
- Git
- GitHub

---




