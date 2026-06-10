import pandas as pd

df = pd.read_csv(
    "data/processed/01_combined.csv",
    sep="\t"
)

print("Original rows:", len(df))

# Fill missing values
df = df.ffill().bfill()

# Remove duplicate timestamps
df = df.drop_duplicates(subset=["timestamp"])

# Remove rows with missing yield
df = df.dropna(subset=["yield"])

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