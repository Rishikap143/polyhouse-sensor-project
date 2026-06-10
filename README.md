# Polyhouse Sensor Project

## Objective

This project processes polyhouse sensor data, performs data cleaning, exploratory data analysis (EDA), and feature engineering to prepare data for crop yield prediction using machine learning.

---

## Project Structure

```text
polyhouse-sensor-project/

├── data/
│   ├── raw/
│   │   ├── climate_data.csv
│   │   ├── polyhouse_sensor.csv
│   │   └── yield_data.csv
│   │
│   └── processed/
│       ├── 01_combined.csv
│       ├── 02_cleaned.parquet
│       ├── sample_cleaned_data.csv
│       ├── X_train.parquet
│       ├── X_test.parquet
│       ├── y_train.parquet
│       └── y_test.parquet
│
├── docs/
│   └── cleaning_log.md
│
├── models/
│   └── scaler.joblib
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
│   ├── eda.py
│   └── features.py
│
└── README.md
```

---

## Features

### Task 2 – Data Cleaning

* Loads raw sensor, climate, and yield datasets.
* Audits missing values.
* Cleans and preprocesses data.
* Generates cleaned dataset in Parquet format.
* Produces sample cleaned dataset.
* Documents all cleaning decisions.

### Task 3 – Exploratory Data Analysis (EDA)

* Generates descriptive statistics.
* Produces data quality report.
* Creates correlation heatmap.
* Creates scatter plots for:

  * Humidity vs Yield
  * CO₂ vs Yield
  * Temperature vs Yield
* Documents insights from environmental variables and crop yield.

### Task 4 – Feature Engineering

* Creates machine learning features from cleaned data.
* Engineers interaction feature between temperature and humidity.
* Performs chronological train/test split.
* Applies MinMaxScaler using training data only.
* Saves scaler for future model inference.
* Saves train/test artifacts for model training.

---

## Data Cleaning Strategy

* Temperature: Missing values imputed using median.
* Humidity: Missing values imputed using median.
* CO₂: Missing values imputed using median.
* Yield: Rows with missing target values removed.

Cleaning rationale is documented in:

```text
docs/cleaning_log.md
```

---

## Key EDA Insights

### Humidity and Yield

Humidity values range from 57% to 69%. Yield remains relatively stable across this range, indicating a moderate relationship between humidity and crop yield.

### CO₂ and Yield

Higher CO₂ levels generally correspond to slightly higher yield values, suggesting that increased CO₂ concentration may support plant growth inside the polyhouse environment.

### Temperature and Yield

Temperature remains within a narrow range. Yield variation is limited, indicating relatively stable growing conditions.

### Correlation Notes

* Correlation heatmap was generated to identify relationships among variables.
* Correlation does not imply causation.
* Results should be interpreted carefully because of the dataset size.

---

## Feature Engineering

### Engineered Feature

```text
temp_humid_interaction = (temperature × humidity) / 100
```

This feature captures the combined influence of temperature and humidity on crop growth conditions.

### Feature Columns

| Feature                | Description                    |
| ---------------------- | ------------------------------ |
| temperature            | Greenhouse temperature reading |
| humidity               | Greenhouse humidity reading    |
| CO2                    | Carbon dioxide concentration   |
| temp_humid_interaction | (temperature × humidity) / 100 |

### Target Variable

```text
yield
```

### Feature Validation

* No missing values after feature engineering.
* X and y shapes validated before processing.
* Data sorted chronologically using timestamp.
* Feature matrix successfully prepared for modeling.

### Scaling

MinMaxScaler is used to normalize feature values.

Formula:

```text
X_scaled = (X - X_min) / (X_max - X_min)
```

Result:

```text
0 ≤ X_scaled ≤ 1
```

---

## Temporal Train/Test Split

The dataset is sorted chronologically using the timestamp column before splitting.

### Split Strategy

* Training Set: First 80% of observations
* Test Set: Last 20% of observations

### Data Leakage Prevention

The MinMaxScaler is fitted only on the training data.

```text
scaler.fit(X_train)
```

The same scaler is then applied to the test data:

```text
scaler.transform(X_test)
```

This prevents information from the test set leaking into the training process.

### Saved Artifacts

```text
data/processed/X_train.parquet
data/processed/X_test.parquet
data/processed/y_train.parquet
data/processed/y_test.parquet
```

### Saved Scaler

```text
models/scaler.joblib
```

---

## Output Files

### Cleaned Dataset

```text
data/processed/02_cleaned.parquet
```

### Training Features

```text
data/processed/X_train.parquet
```

### Testing Features

```text
data/processed/X_test.parquet
```

### Training Target

```text
data/processed/y_train.parquet
```

### Testing Target

```text
data/processed/y_test.parquet
```

### Saved Scaler

```text
models/scaler.joblib
```

### Cleaning Log

```text
docs/cleaning_log.md
```

### Data Quality Report

```text
reports/data_quality.md
```

### EDA Summary

```text
reports/eda_summary.md
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

### Feature Engineering

```bash
python src/features.py
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Parquet
* Git
* GitHub





