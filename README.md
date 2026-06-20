# Polyhouse Mushroom Yield Forecasting

## Live Deployment

**Streamlit App:**
https://polyhouse-yield-predictor.streamlit.app

This application predicts mushroom yield (kg) using environmental sensor readings collected from a polyhouse.

---

## Overview

The project implements an end-to-end machine learning workflow for mushroom yield prediction:

* Data ingestion
* Data cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Linear Regression baseline model
* Random Forest model
* Hyperparameter tuning using GridSearchCV
* Champion model selection
* Streamlit deployment
* Yield prediction inference

---

## Project Structure

```text
polyhouse-sensor-project-master/

├── app.py
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── cleaning_log.md
│   └── monitoring.md
│
├── models/
│   ├── champion.joblib
│   ├── feature_cols.json
│   ├── random_forest.joblib
│   ├── linear_regression.joblib
│   ├── scaler.joblib
│   └── rf_best_params.json
│
├── reports/
│   ├── figures/
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
├── .runtime.txt
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

GridSearchCV parameter grid:

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

**Tuned Random Forest Regressor**

Reason:

The tuned Random Forest achieved the lowest MAE and RMSE on the untouched test set and was selected as the production model.

Saved artifacts:

```text
models/champion.joblib
models/feature_cols.json
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

## Running the Streamlit App

Run locally:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Cloud Deployment

The application is deployed on Streamlit Community Cloud:

https://polyhouse-yield-predictor.streamlit.app

Deployment requirements:

* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib

Python version is pinned using:

```text
.runtime.txt
```

---

## Model Artifact Handling

The application loads model artifacts directly from the repository:

```text
models/champion.joblib
models/feature_cols.json
```

These files are committed to GitHub and automatically loaded during deployment.

---

## Monitoring Plan

Prediction monitoring is documented in:

```text
docs/monitoring.md
```

The monitoring plan includes:

* Prediction log samples
* Input monitoring
* Retraining triggers
* Model maintenance strategy

Suggested retraining triggers:

* Significant increase in prediction error
* New sensor value ranges outside training distribution
* Monthly model review
* Collection of substantial new production data

---

## Generated Reports

The project automatically generates:

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

* Predictions may be less reliable outside the training data range.
* Seasonal effects are not explicitly modeled.
* Additional environmental variables may improve performance.
* Results depend on sensor quality and calibration.

---

## Reproducibility

To reproduce the complete workflow:

```bash
pip install -r requirements.txt

python src/ingest_data.py
python src/clean_data.py
python src/features.py
python src/eda.py
python src/train_rf_tuned.py
```
