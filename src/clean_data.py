import pandas as pd

<<<<<<< HEAD
df = pd.read_csv(
    "data/processed/01_combined.csv",
    sep="\t"
)

print("Original rows:", len(df))

# Fill missing values
df = df.ffill().bfill()
=======
df = pd.read_csv("data/processed/01_combined.csv")

print("Original rows:", len(df))

# Fill missing sensor values
sensor_cols = [
    "temperature",
    "humidity",
    "soil_moisture",
    "light_intensity",
    "co2"
]

df[sensor_cols] = df[sensor_cols].ffill().bfill()

# Fill crop type if missing
df["crop_type"] = df["crop_type"].fillna("Tomato")

# Remove rows with missing yield
df = df.dropna(subset=["yield_kg"])
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a

# Remove duplicate timestamps
df = df.drop_duplicates(subset=["timestamp"])

<<<<<<< HEAD
# Remove rows with missing yield
df = df.dropna(subset=["yield"])

=======
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
# Save cleaned dataset
df.to_parquet(
    "data/processed/02_cleaned.parquet",
    index=False
)

# Save sample (50 rows)
df.head(50).to_csv(
    "data/processed/sample_cleaned_data.csv",
    index=False
)

print("Cleaning complete!")
print("Rows remaining:", len(df))