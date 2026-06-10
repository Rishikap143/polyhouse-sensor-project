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

# Load cleaned dataset
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Sort chronologically
df = df.sort_values("timestamp")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Feature engineering
df["temp_humid_interaction"] = (
    df["temperature"] * df["humidity"] / 100
)

# Feature columns
feature_cols = [
    "temperature",
    "humidity",
    "CO2",
    "temp_humid_interaction"
]

# Temporal split (80% train, 20% test)
split_idx = int(len(df) * 0.8)

train_df = df.iloc[:split_idx]
test_df = df.iloc[split_idx:]

print("Train rows:", len(train_df))
print("Test rows:", len(test_df))

print(
    "Train date range:",
    train_df["timestamp"].min(),
    "to",
    train_df["timestamp"].max()
)

print(
    "Test date range:",
    test_df["timestamp"].min(),
    "to",
    test_df["timestamp"].max()
)

# Create X and y
X_train = train_df[feature_cols]
X_test = test_df[feature_cols]

y_train = train_df["yield"]
y_test = test_df["yield"]

# Validate shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Check for missing values
assert X_train.isna().sum().sum() == 0, "X_train contains NaN values"
assert X_test.isna().sum().sum() == 0, "X_test contains NaN values"

assert y_train.isna().sum() == 0, "y_train contains NaN values"
assert y_test.isna().sum() == 0, "y_test contains NaN values"

print("No NaN values found")

# Create models folder if missing
Path("models").mkdir(exist_ok=True)

# Scale features using TRAIN ONLY
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Minimum scaled value:", X_train_scaled.min())
print("Maximum scaled value:", X_train_scaled.max())

# Save scaler
joblib.dump(
    scaler,
    "models/scaler.joblib"
)

print("Scaler saved successfully")

# Save train features
pd.DataFrame(
    X_train_scaled,
    columns=[c + "_scaled" for c in feature_cols]
).to_parquet(
    "data/processed/X_train.parquet",
    index=False
)

# Save test features
pd.DataFrame(
    X_test_scaled,
    columns=[c + "_scaled" for c in feature_cols]
).to_parquet(
    "data/processed/X_test.parquet",
    index=False
)

# Save train target
y_train.to_frame().to_parquet(
    "data/processed/y_train.parquet",
    index=False
)

# Save test target
y_test.to_frame().to_parquet(
    "data/processed/y_test.parquet",
    index=False
)

print("Train/Test artifacts saved successfully")
print("Feature engineering completed")