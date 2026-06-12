from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/processed/sample_cleaned_data.csv")

# Features
X = df[["temperature", "humidity", "CO2"]]

# Target
y = df["yield"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False
)

# -----------------------------
# Train Random Forest
# -----------------------------
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

# Predictions
train_pred = rf.predict(X_train)
test_pred = rf.predict(X_test)

# Metrics
train_mae = mean_absolute_error(y_train, train_pred)
test_mae = mean_absolute_error(y_test, test_pred)
test_r2 = r2_score(y_test, test_pred)

print(f"RF Train MAE: {train_mae:.2f} kg")
print(f"RF Test MAE:  {test_mae:.2f} kg")
print(f"RF Test R²:   {test_r2:.3f}")

# -----------------------------
# Feature Importance Plot
# -----------------------------
importances = rf.feature_importances_
labels = ["temperature", "humidity", "co2"]

plt.figure(figsize=(6, 4))
plt.barh(labels, importances)
plt.xlabel("Importance")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("reports/figures/rf_importance.png", dpi=150)
plt.close()

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(rf, "models/random_forest.joblib")

# -----------------------------
# Time Series Cross Validation
# -----------------------------
tscv = TimeSeriesSplit(n_splits=5)

rf_cv_scores = cross_val_score(
    RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    ),
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

lin_cv_scores = cross_val_score(
    LinearRegression(),
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

rf_mae_scores = -rf_cv_scores
lin_mae_scores = -lin_cv_scores

print("\n----- TimeSeriesSplit Results -----")

print("RF Fold MAE Scores:")
print(rf_mae_scores)

print(
    f"RF CV MAE: {rf_mae_scores.mean():.3f} "
    f"+/- {rf_mae_scores.std():.3f}"
)

print("\nLinear Regression Fold MAE Scores:")
print(lin_mae_scores)

print(
    f"Linear CV MAE: {lin_mae_scores.mean():.3f} "
    f"+/- {lin_mae_scores.std():.3f}"
)

# -----------------------------
# Overfitting Analysis
# -----------------------------
print("\n----- Overfitting Check -----")
print(f"Train MAE: {train_mae:.3f}")
print(f"Test MAE : {test_mae:.3f}")

if test_mae - train_mae > 0.05:
    print("Possible overfitting detected.")
else:
    print("No significant overfitting detected.")