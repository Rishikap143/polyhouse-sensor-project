# Monitoring Plan

## Prediction Logging

The application logs prediction requests to `prediction_log.csv`.

### Sample Log Entry

| Timestamp           | Temperature (°C) | Humidity (%) | CO₂ (ppm) | Prediction (kg) |
| ------------------- | ---------------- | ------------ | --------- | --------------- |
| 2026-06-19 13:01:20 | 22.0             | 88.0         | 900       | 1.01            |

### Logged Fields

* Timestamp
* Temperature
* Humidity
* CO₂
* Predicted Yield

## Model Artifact Handling

The trained model artifacts are stored in the `models/` directory:

* champion.joblib
* feature_cols.json

These files are loaded automatically by the Streamlit application using `joblib`.

## Monitoring Metrics

The following metrics should be monitored:

* Number of predictions per day
* Average predicted yield
* Input feature distributions
* Prediction trends over time

## Retraining Triggers

The model should be retrained when:

1. New sensor data exceeds 500 records.
2. Prediction accuracy decreases significantly.
3. Input distributions drift from training data.
4. Monthly performance review identifies degradation.

## Validation

* Streamlit predictions match CLI predictions.
* Prediction logs are generated successfully.
* Missing model files display a user-friendly error message.
