"""
Feature Engineering

Features:
temperature = greenhouse temperature reading
humidity = greenhouse humidity reading
CO2 = carbon dioxide concentration

temp_humid_interaction =
temperature * humidity / 100

Target:
yield
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

# ==========================
# Load cleaned dataset
# ==========================
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Convert timestamp FIRST
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Then sort chronologically
df = df.sort_values("timestamp").reset_index(drop=True)

# ==========================
# Feature Engineering
# ==========================
df["temp_humid_interaction"] = (
    df["temperature"] * df["humidity"] / 100
)

feature_cols = [
    "temperature",
    "humidity",
    "CO2",
    "temp_humid_interaction"
]

# Debug: verify chronological order
print("First timestamp:", df["timestamp"].iloc[0])
print("Last timestamp:", df["timestamp"].iloc[-1])

# ==========================
# Temporal Train/Test Split
# ==========================
split_idx = int(len(df) * 0.8)

train_df = df.iloc[:split_idx]
test_df = df.iloc[split_idx:]

print("\nTrain size:", len(train_df))
print("Test size:", len(test_df))

print("Train starts:", train_df["timestamp"].min())
print("Train ends:", train_df["timestamp"].max())

print("Test starts:", test_df["timestamp"].min())
print("Test ends:", test_df["timestamp"].max())

print("Chronological split complete")

# ==========================
# Create X and y
# ==========================
X_train = train_df[feature_cols]
X_test = test_df[feature_cols]

y_train = train_df["yield"]
y_test = test_df["yield"]

# ==========================
# Missing Value Check
# ==========================
print("\nFeature Columns:")
print(X_train.columns)

print("\nMissing Values:")
print(X_train.isnull().sum())

assert X_train.isna().sum().sum() == 0
assert X_test.isna().sum().sum() == 0
assert y_train.isna().sum() == 0
assert y_test.isna().sum() == 0

# ==========================
# Scaling (TRAIN ONLY)
# ==========================
Path("models").mkdir(exist_ok=True)

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nMinimum Values After Scaling:")
print(pd.Series(X_train_scaled.min(axis=0), index=feature_cols))

print("\nMaximum Values After Scaling:")
print(pd.Series(X_train_scaled.max(axis=0), index=feature_cols))

print("\nX shape:", X_train.shape)
print("y shape:", y_train.shape)

# ==========================
# Save scaler
# ==========================
joblib.dump(scaler, "models/scaler.joblib")

print("\nScaler saved successfully")

# ==========================
# Save train/test features
# ==========================
pd.DataFrame(
    X_train_scaled,
    columns=feature_cols
).to_parquet(
    "data/processed/X_train.parquet",
    index=False
)

pd.DataFrame(
    X_test_scaled,
    columns=feature_cols
).to_parquet(
    "data/processed/X_test.parquet",
    index=False
)

# ==========================
# Save targets
# ==========================
y_train.to_frame().to_parquet(
    "data/processed/y_train.parquet",
    index=False
)

y_test.to_frame().to_parquet(
    "data/processed/y_test.parquet",
    index=False
)

print("Train/Test artifacts saved successfully")
print("Feature engineering completed")