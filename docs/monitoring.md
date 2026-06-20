# Model Monitoring Plan

## Purpose

This document describes the monitoring strategy for the Polyhouse Mushroom Yield Forecasting application deployed on Streamlit Community Cloud.

The goal is to ensure prediction quality, detect data drift, and define clear retraining triggers for the champion model.

---

## Current Production Model

**Champion Model:** Tuned Random Forest Regressor

Model Artifact:

```text
models/champion.joblib
```

Feature Configuration:

```text
models/feature_cols.json
```

Input Features:

* Temperature (°C)
* Humidity (%)
* CO₂ (ppm)

Output:

* Predicted Mushroom Yield (kg)

---

## Prediction Logging

For every prediction request, the following information should be recorded:

| Timestamp        | Temperature (°C) | Humidity (%) | CO₂ (ppm) | Predicted Yield (kg) |
| ---------------- | ---------------- | ------------ | --------- | -------------------- |
| 2026-06-20 14:05 | 22.0             | 88.0         | 900       | 3.42                 |

Example Log Entry:

```json
{
  "timestamp": "2026-06-20T14:05:00",
  "temperature_c": 22.0,
  "humidity_pct": 88.0,
  "co2_ppm": 900,
  "predicted_yield_kg": 3.42
}
```

---

## Monitoring Metrics

The following metrics should be reviewed regularly:

### Input Monitoring

Track the distribution of:

* Temperature
* Humidity
* CO₂

Watch for:

* Values outside the training range
* Unexpected spikes
* Missing values
* Sensor malfunctions

### Prediction Monitoring

Track:

* Average predicted yield
* Minimum predicted yield
* Maximum predicted yield
* Prediction distribution over time

Watch for:

* Sudden shifts in predictions
* Unusually high or low values
* Changes in prediction patterns

---

## Data Drift Detection

Potential data drift indicators:

* Temperature range differs significantly from training data.
* Humidity distribution changes over time.
* CO₂ levels consistently exceed historical values.
* New environmental conditions not represented in training data.

If significant drift is detected, retraining should be considered.

---

## Retraining Triggers

The model should be retrained if any of the following occur:

### Performance Trigger

* Mean Absolute Error (MAE) increases by more than 20% compared to baseline.

### Data Drift Trigger

* Input feature distributions shift significantly from historical data.

### Volume Trigger

* More than 1,000 new production records become available.

### Scheduled Trigger

* Quarterly review and model retraining.

---

## Alert Conditions

Investigate the system if:

* Predictions become consistently unrealistic.
* Sensor readings fall outside expected operational ranges.
* Model files become corrupted or unavailable.
* Prediction requests begin failing.

---

## Maintenance Plan

### Weekly

* Review prediction logs.
* Check for unusual sensor values.

### Monthly

* Review prediction distributions.
* Evaluate model performance using available ground-truth data.

### Quarterly

* Retrain and validate the model if new data is available.
* Compare challenger models against the current champion model.

---

## Deployment Information

Deployment Platform:

* Streamlit Community Cloud

Live Application:

* https://polyhouse-yield-predictor.streamlit.app

Repository:

* GitHub Repository containing source code, model artifacts, and deployment configuration.

---

## Conclusion

The monitoring process helps ensure that the deployed mushroom yield prediction model remains reliable, accurate, and relevant as new environmental data becomes available.
