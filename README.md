# Polyhouse Mushroom Yield Forecasting

## Overview

This project predicts mushroom yield (kg) using environmental sensor data collected from a polyhouse.

The workflow includes:

* Data ingestion
* Data cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Linear Regression baseline model
* Random Forest model
* Hyperparameter tuning using GridSearchCV
* Champion model selection
* Yield prediction inference

---

## Project Structure

```text
polyhouse-sensor-project-master/

├── data/
│   ├── raw/
│   └── processed/
│       ├── 01_combined.csv
│       ├── 02_cleaned.parquet
│       ├── features.parquet
│       ├── X_train.parquet
│       ├── X_test.parquet
│       ├── y_train.parquet
│       └── y_test.parquet
│
├── docs/
│   └── cleaning_log.md
│
├── models/
│   ├── champion.joblib
│   ├── random_forest.joblib
│   ├── linear_regression.joblib
│   ├── scaler.joblib
│   ├── minmax_scaler.joblib
│   ├── feature_cols.json
│   └── rf_best_params.json
│
├── reports/
│   ├── figures/
│   │   ├── correlation_heatmap.png
│   │   ├── temperature_vs_yield.png
│   │   ├── humidity_vs_yield.png
│   │   ├── co2_vs_yield.png
│   │   ├── pred_vs_actual.png
│   │   ├── residuals_linear.png
│   │   └── rf_importance.png
│   │
│   ├── eda_summary.md
│   ├── data_quality.md
│   ├── linear_diagnostics.md
│   ├── rf_summary.md
│   ├── metrics_linear.json
│   ├── rf_tuned_metrics.json
│   └── model_comparison.csv
│
├── src/
│   ├── ingest_data.py
│   ├── clean_data.py
│   ├── features.py
│   ├── eda.py
│   ├── predict.py
│   └── train_rf_tuned.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run the Random Forest tuning pipeline:

```bash
python src/train_rf_tuned.py
```

Outputs:

* Tuned Random Forest model
* Champion model
* Best hyperparameters
* Evaluation metrics
* Comparison report
* Predicted vs Actual plot

---

## Hyperparameter Tuning

GridSearchCV was performed using the following parameter grid:

```python
{
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5]
}
```

Best Parameters:

```json
{
    "max_depth": 8,
    "min_samples_leaf": 1,
    "n_estimators": 200
}
```

---

## Model Performance

| Model                 | MAE    | RMSE   | R²     |
| --------------------- | ------ | ------ | ------ |
| Linear Regression     | 0.0704 | 0.0995 | 0.8015 |
| Random Forest Default | 0.0800 | 0.1100 | 0.4700 |
| Random Forest Tuned   | 0.0536 | 0.0942 | 0.5288 |

---

## Champion Model

Champion Model:

**Tuned Random Forest Regressor**

Reason:

The tuned Random Forest achieved the lowest MAE and RMSE on the untouched test set, providing the most accurate yield predictions.

Saved as:

```text
models/champion.joblib
```

---

## Running Inference

Example:

```python
from src.predict import predict_yield

yield_prediction = predict_yield(
    temperature_c=24.5,
    humidity_pct=85.0,
    co2_ppm=900
)

print(f"Predicted Yield: {yield_prediction:.2f} kg")
```

Example Output:

```text
Predicted Yield: 3.42 kg
```

---

## Generated Reports

The project automatically creates:

* Correlation heatmap
* Feature relationship plots
* Feature importance plot
* Residual analysis
* Predicted vs Actual plot
* EDA summary
* Model comparison report

All reports are stored in:

```text
reports/
```

---

## Limitations

* Predictions may be less reliable when sensor values fall outside the training range.
* Seasonal effects are not explicitly modeled.
* Additional environmental variables may improve prediction accuracy.
* Performance depends on the quality of sensor measurements.

---

## Reproducibility

To reproduce the entire workflow:

```bash
pip install -r requirements.txt
python src/ingest_data.py
python src/clean_data.py
python src/features.py
python src/eda.py
python src/train_rf_tuned.py
```
