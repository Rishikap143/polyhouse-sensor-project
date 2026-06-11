from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import numpy as np
import json
from pathlib import Path
import pandas as pd

# Load train/test datasets
X_train = pd.read_parquet("data/processed/X_train.parquet")
X_test = pd.read_parquet("data/processed/X_test.parquet")

y_train = pd.read_parquet("data/processed/y_train.parquet").squeeze()
y_test = pd.read_parquet("data/processed/y_test.parquet").squeeze()

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
pred_test = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, pred_test)
rmse = np.sqrt(mean_squared_error(y_test, pred_test))
r2 = r2_score(y_test, pred_test)

print(f"Test MAE:  {mae:.2f} kg")
print(f"Test RMSE: {rmse:.2f} kg")
print(f"Test R²:   {r2:.3f}")

# Save metrics
Path("reports").mkdir(exist_ok=True)

metrics = {
    "MAE": float(mae),
    "RMSE": float(rmse),
    "R2": float(r2)
}

with open("reports/metrics_linear.json", "w") as f:
    json.dump(metrics, f, indent=4)

# Print coefficients
for name, coef in zip(["temp", "humidity", "co2"], model.coef_):
    print(f"coef {name}: {coef:.3f}")

# Save model
joblib.dump(model, "models/linear_regression.joblib")
import matplotlib.pyplot as plt

residuals = y_test - pred_test

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Residuals vs Predicted
axes[0].scatter(pred_test, residuals, alpha=0.5)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set(
    xlabel="Predicted Yield (kg)",
    ylabel="Residual (kg)"
)

# Residuals vs Humidity
axes[1].scatter(X_test["humidity"], residuals, alpha=0.5)
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set(
    xlabel="Scaled Humidity",
    ylabel="Residual (kg)"
)

plt.tight_layout()
plt.savefig("reports/figures/residuals_linear.png", dpi=150)
plt.close()

print("Residual diagnostics saved")