import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")
PROCESSED.mkdir(parents=True, exist_ok=True)

# Load files
sensor = pd.read_csv(RAW / "polyhouse_sensor.csv")
yield_df = pd.read_csv(RAW / "yield_data.csv")

# Convert timestamp to datetime
sensor["timestamp"] = pd.to_datetime(sensor["timestamp"])

# Extract date from timestamp
sensor["date"] = sensor["timestamp"].dt.date

# Convert yield date column
yield_df["date"] = pd.to_datetime(yield_df["date"]).dt.date

# Merge on date
combined = pd.merge(
    sensor,
    yield_df,
    on="date",
    how="left"
)

print("Combined shape:", combined.shape)
print(combined.head())

combined.to_csv(
    PROCESSED / "01_combined.csv",
    index=False
)

print("Saved data/processed/01_combined.csv")