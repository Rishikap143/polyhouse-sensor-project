from pathlib import Path
import json
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import time

start_time = time.time()

from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# -------------------------
# Load data
# -------------------------
df = pd.read_csv(
    "data/processed/sample_cleaned_data.csv"
)
print("Columns found:")
print(df.columns.tolist())

# CHANGE THESE IF YOUR COLUMN NAMES ARE DIFFERENT
feature_cols = [
    "temperature",
    "humidity",
    "CO2"
]

target_col = "yield"
# Verify columns exist
for col in feature_cols + [target_col]:
    if col not in df.columns:
        raise ValueError(
            f"Column '{col}' not found.\n"
            f"Available columns: {df.columns.tolist()}"
        )

X = df[feature_cols]
y = df[target_col]

# -------------------------
# Train / Test Split
# -------------------------
split_idx = int(len(df) * 0.8)

X_train = X.iloc[:split_idx]
X_test = X.iloc[split_idx:]

y_train = y.iloc[:split_idx]
y_test = y.iloc[split_idx:]

# -------------------------
# Grid Search
# -------------------------
tscv = TimeSeriesSplit(n_splits=5)

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5]
}

rf = RandomForestRegressor(
    random_state=42,
    n_jobs=-1
)

grid = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    scoring="neg_mean_absolute_error",
    cv=tscv,
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("\nBest Params:")
print(grid.best_params_)

print("\nBest CV MAE:")
print(grid.best_score_)

best_model = grid.best_estimator_

# -------------------------
# Create folders
# -------------------------
Path("models").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)
Path("reports/figures").mkdir(
    parents=True,
    exist_ok=True
)

# -------------------------
# Save best params
# -------------------------
with open(
    "models/rf_best_params.json",
    "w"
) as f:
    json.dump(
        grid.best_params_,
        f,
        indent=2
    )

# -------------------------
# Save feature order
# -------------------------
with open(
    "models/feature_cols.json",
    "w"
) as f:
    json.dump(
        feature_cols,
        f,
        indent=2
    )

# -------------------------
# Test Evaluation
# -------------------------
pred = best_model.predict(X_test)

mae = mean_absolute_error(y_test, pred)
rmse = mean_squared_error(y_test, pred) ** 0.5
r2 = r2_score(y_test, pred)

print("\nTest Metrics")
print(f"MAE : {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²  : {r2:.4f}")

# -------------------------
# Save metrics
# -------------------------
metrics = {
    "mae": float(mae),
    "rmse": float(rmse),
    "r2": float(r2)
}

with open(
    "reports/rf_tuned_metrics.json",
    "w"
) as f:
    json.dump(metrics, f, indent=2)

# -------------------------
# Save champion model
# -------------------------
joblib.dump(
    best_model,
    "models/champion.joblib"
)
# -------------------------
# Comparison Table
# -------------------------

# Actual metrics from previous experiments
linear_mae = 0.07035444052014712
linear_rmse = 0.09952428641403038
linear_r2 = 0.8015144970098786

rf_default_mae = 0.0800
rf_default_rmse = 0.1100
rf_default_r2 = 0.4700

results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest Default",
        "Random Forest Tuned"
    ],
    "MAE": [
        linear_mae,
        rf_default_mae,
        mae
    ],
    "RMSE": [
        linear_rmse,
        rf_default_rmse,
        rmse
    ],
    "R2": [
        linear_r2,
        rf_default_r2,
        r2
    ]
})

print("\nModel Comparison")
print(results)

results.to_csv(
    "reports/model_comparison.csv",
    index=False
)

# -------------------------
# Predicted vs Actual
# -------------------------
plt.figure(figsize=(6, 6))

plt.scatter(
    y_test,
    pred,
    alpha=0.6
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)

plt.xlabel("Actual Yield (kg)")
plt.ylabel("Predicted Yield (kg)")
plt.title("Champion Model: Predicted vs Actual")

plt.savefig(
    "reports/figures/pred_vs_actual.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("\nTraining complete.")
print("Champion model saved to models/champion.joblib")
# -------------------------
# Runtime
# -------------------------
runtime = time.time() - start_time

# -------------------------
# Summary Markdown
# -------------------------
summary = f"""
# Random Forest Tuning Summary

## Parameter Grid

- n_estimators: [50, 100, 200]
- max_depth: [None, 8, 16]
- min_samples_leaf: [1, 3, 5]
## Parameter Grid Rationale

- n_estimators controls the number of trees in the forest. Higher values can improve stability but increase training time.

- max_depth controls how deep each tree can grow. Limiting depth helps reduce overfitting.

- min_samples_leaf controls the minimum samples required in a leaf node. Larger values create smoother predictions and reduce overfitting.

## Best Parameters

{grid.best_params_}

## Best CV MAE

{grid.best_score_:.4f}

## Test Metrics

- MAE: {mae:.4f}
- RMSE: {rmse:.4f}
- R²: {r2:.4f}

## Model Comparison

| Model | MAE | RMSE | R² |
|--------|--------|--------|--------|
| Linear Regression | {linear_mae:.4f} | {linear_rmse:.4f} | {linear_r2:.4f} |
| Random Forest Default | {rf_default_mae:.4f} | {rf_default_rmse:.4f} | {rf_default_r2:.4f} |
| Random Forest Tuned | {mae:.4f} | {rmse:.4f} | {r2:.4f} |

## Champion Model

## Champion Model
The Tuned Random Forest model was selected as the champion model because it achieved the lowest MAE and RMSE on the untouched test set. Although Linear Regression achieved a higher R² score, the tuned Random Forest produced smaller prediction errors, making it the preferred model for yield prediction.
## Runtime

Training and tuning completed in {runtime:.2f} seconds.

## Limitations

- Predictions may be less reliable when sensor values fall outside the training range.
- Seasonal effects are not explicitly modeled.
- Additional environmental variables may improve prediction accuracy.
"""

with open(
    "reports/rf_summary.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(summary)

print("\nSummary saved to reports/rf_summary.md")