# Polyhouse Sensor Project

## Objective

<<<<<<< HEAD
This project processes polyhouse sensor data, performs data cleaning, exploratory data analysis (EDA), and feature engineering to prepare data for crop yield prediction using machine learning.
=======
This project processes polyhouse sensor data, performs data cleaning, and conducts exploratory data analysis (EDA) to understand relationships between environmental conditions and crop yield.
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a

---

## Project Structure

<<<<<<< HEAD
```text
polyhouse-sensor-project/

=======
```
polyhouse-sensor-project/
│
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
├── data/
│   ├── raw/
│   │   ├── climate_data.csv
│   │   ├── polyhouse_sensor.csv
│   │   └── yield_data.csv
│   │
│   └── processed/
│       ├── 01_combined.csv
│       ├── 02_cleaned.parquet
<<<<<<< HEAD
│       ├── sample_cleaned_data.csv
│       ├── X_train.parquet
│       ├── X_test.parquet
│       ├── y_train.parquet
│       └── y_test.parquet
=======
│       └── sample_cleaned_data.csv
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
│
├── docs/
│   └── cleaning_log.md
│
<<<<<<< HEAD
├── models/
│   └── scaler.joblib
│
=======
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
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
<<<<<<< HEAD
│   ├── eda.py
│   └── features.py
=======
│   └── eda.py
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
│
└── README.md
```

---

## Features

### Task 2 – Data Cleaning

<<<<<<< HEAD
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
=======
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
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a

---

## Data Cleaning Strategy

<<<<<<< HEAD
* Temperature: Missing values imputed using median.
* Humidity: Missing values imputed using median.
* CO₂: Missing values imputed using median.
* Yield: Rows with missing target values removed.

Cleaning rationale is documented in:

```text
=======
- Temperature: Missing values imputed using median.
- Humidity: Missing values imputed using median.
- CO₂: Missing values imputed using median.
- Yield: Rows with missing target values removed.

Cleaning rationale is documented in:

```
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
docs/cleaning_log.md
```

---

<<<<<<< HEAD
=======
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

>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
## Key EDA Insights

### Humidity and Yield

Humidity values range from 57% to 69%. Yield remains relatively stable across this range, indicating a moderate relationship between humidity and crop yield.

### CO₂ and Yield

Higher CO₂ levels generally correspond to slightly higher yield values, suggesting that increased CO₂ concentration may support plant growth inside the polyhouse environment.

### Temperature and Yield

<<<<<<< HEAD
Temperature remains within a narrow range. Yield variation is limited, indicating relatively stable growing conditions.

### Correlation Notes

* Correlation heatmap was generated to identify relationships among variables.
* Correlation does not imply causation.
* Results should be interpreted carefully because of the dataset size.

---

## Feature Engineering

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

* No missing values detected after feature engineering.
* Dataset sorted chronologically before train/test split.
* Training set contains 400 observations.
* Testing set contains 100 observations.
* Feature matrix shape: (400, 4)
* Target vector shape: (400,)
* MinMaxScaler fitted using training data only.
* Scaler saved successfully for future inference.

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

The dataset was sorted chronologically using the timestamp column before splitting.

### Split Strategy

* Training Set: First 80% of observations
* Test Set: Last 20% of observations

### Split Summary

| Dataset | Rows | Start Date          | End Date            |
| ------- | ---- | ------------------- | ------------------- |
| Train   | 400  | 2025-01-01 06:00:00 | 2025-01-17 21:00:00 |
| Test    | 100  | 2025-01-17 22:00:00 | 2025-01-22 01:00:00 |

### Data Leakage Prevention

The MinMaxScaler was fitted only on the training data.

```python
scaler.fit(X_train)
```

The same scaler was then applied to the test data.

```python
X_test_scaled = scaler.transform(X_test)
```

This prevents information from the test dataset leaking into the training process.

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
=======
Temperature remains within a narrow range (26.5°C–32.4°C). Yield variation is limited, indicating relatively stable growing conditions.

### Correlation Notes

- Correlation heatmap was generated to identify relationships among variables.
- Correlation does not imply causation.
- The dataset contains only 50 observations, so conclusions should be interpreted carefully.

---

## Output Files

### Cleaned Dataset

<<<<<<< HEAD
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
=======
```
data/processed/02_cleaned.parquet
```

### Sample Dataset

```
data/processed/sample_cleaned_data.csv
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
```

### Cleaning Log

<<<<<<< HEAD
```text
=======
docs/cleaning_log.md
```

### Data Quality Report

<<<<<<< HEAD
```text
=======
```
reports/data_quality.md
```

### EDA Summary

<<<<<<< HEAD
```text
reports/eda_summary.md
```

=======
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

<<<<<<< HEAD
### Feature Engineering

```bash
python src/features.py
```

=======
---

## Technologies Used

<<<<<<< HEAD
* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Parquet
* Git
* GitHub

=======
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Parquet
- Git
- GitHub

---





