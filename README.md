# Polyhouse Sensor Project

## Objective

This project processes polyhouse sensor data, performs data cleaning, exploratory data analysis (EDA), feature engineering, and machine learning modeling to prepare data for crop yield prediction.

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
│   ├── linear_metrics.json
│   └── figures/
│       ├── correlation_heatmap.png
│       ├── humidity_vs_yield.png
│       ├── co2_vs_yield.png
│       ├── temperature_vs_yield.png
│       └── rf_feature_importance.png
│
├── src/
│   ├── ingest_data.py
│   ├── clean_data.py
│   ├── eda.py
│   ├── features.py
│   ├── train_linear.py
│   └── train_random_forest.py
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

### Task 5 – Linear Regression Baseline

* Trains an interpretable Linear Regression model.
* Evaluates MAE, RMSE, and R² on the test dataset.
* Generates residual diagnostics.
* Produces coefficient interpretation for agritech applications.
* Saves evaluation metrics.

### Task 6 – Random Forest & Time-Series Cross Validation

* Trains a Random Forest Regressor.
* Uses TimeSeriesSplit cross-validation.
* Computes cross-validation MAE scores.
* Generates feature importance visualization.
* Compares performance against the Linear Regression baseline.
* Performs overfitting analysis using train and test metrics.

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

Humidity values remain relatively stable throughout the dataset. Yield variation appears moderate across humidity levels.

### CO₂ and Yield

Higher CO₂ concentrations are generally associated with slightly increased yield values, suggesting a positive relationship.

### Temperature and Yield

Temperature remains within a relatively narrow range, indicating stable growing conditions.

### Correlation Notes

* Correlation heatmap was generated to identify relationships among variables.
* Correlation does not imply causation.
* Results should be interpreted carefully because of dataset size.

---

## Feature Engineering

### Engineered Feature

```text
temp_humid_interaction = (temperature × humidity) / 100
```

### Feature Columns

| Feature                | Description                      |
| ---------------------- | -------------------------------- |
| temperature            | Greenhouse temperature reading   |
| humidity               | Greenhouse humidity reading      |
| co2                    | Carbon dioxide concentration     |
| temp_humid_interaction | Temperature–humidity interaction |

### Target Variable

```text
yield
```

### Scaling

MinMaxScaler is used to normalize feature values.

```text
X_scaled = (X - X_min) / (X_max - X_min)
```

---

## Temporal Train/Test Split

The dataset was sorted chronologically before splitting.

### Split Strategy

* Training Set: First 80% of observations
* Test Set: Last 20% of observations

### Data Leakage Prevention

The MinMaxScaler was fitted only on the training dataset and then applied to the test dataset.

This prevents information leakage from the test set into the training process.

---

## Task 5 – Linear Regression Baseline

### Test Metrics

| Metric | Value   |
| ------ | ------- |
| MAE    | 0.07 kg |
| RMSE   | 0.10 kg |
| R²     | 0.802   |

### Model Interpretation

The Linear Regression model provides an interpretable baseline for mushroom yield prediction.

Feature coefficients indicate the direction and strength of influence of environmental variables on yield.

### Residual Analysis

Residual plots were generated to assess prediction errors and model assumptions.

---

## Task 6 – Random Forest & Time-Series Cross Validation

### Cross-Validation Strategy

TimeSeriesSplit was used to preserve temporal ordering and prevent future observations from influencing past predictions.

### Feature Importance

A feature importance chart was generated and saved as:

```text
reports/rf_feature_importance.png
```

### Cross-Validation Results

| Fold | MAE           |
| ---- | ------------- |
| 1    | To be updated |
| 2    | To be updated |
| 3    | To be updated |
| 4    | To be updated |
| 5    | To be updated |

**Mean CV MAE:** To be updated after training.

### Overfitting Analysis

| Metric | Training Set  | Test Set      |
| ------ | ------------- | ------------- |
| MAE    | To be updated | To be updated |
| RMSE   | To be updated | To be updated |

Interpretation:

* Small train–test gap indicates good generalization.
* Large train–test gap suggests overfitting.

### Comparison with Linear Regression

| Model             | MAE           | RMSE          | R²            |
| ----------------- | ------------- | ------------- | ------------- |
| Linear Regression | 0.07          | 0.10          | 0.802         |
| Random Forest     | To be updated | To be updated | To be updated |

### Complexity Assessment

Random Forest can capture non-linear relationships between environmental variables and yield.

Whether the additional complexity is justified depends on the improvement observed relative to the Linear Regression baseline.

---

## Output Files

### Cleaned Dataset

```text
data/processed/02_cleaned.parquet
```

### Sample Dataset

```text
data/processed/sample_cleaned_data.csv
```

### Training Artifacts

```text
data/processed/X_train.parquet
data/processed/X_test.parquet
data/processed/y_train.parquet
data/processed/y_test.parquet
models/scaler.joblib
```

### Reports

```text
reports/data_quality.md
reports/eda_summary.md
reports/linear_metrics.json
reports/rf_feature_importance.png
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

### Linear Regression

```bash
python src/train_linear.py
```

### Random Forest

```bash
python src/train_random_forest.py
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



