import pandas as pd

# Read combined dataset
df = pd.read_csv("data/processed/01_combined.csv")

# Null count before cleaning
print("Null values BEFORE cleaning:")
print(df.isnull().sum())

# Fill missing values for numeric columns with median
numeric_columns = [
    'temperature',
    'humidity',
    'soil_moisture',
    'light_intensity',
    'co2',
    'yield_kg'
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# Remove rows where timestamp is missing
if 'timestamp' in df.columns:
    df = df.dropna(subset=['timestamp'])

# Fill crop_type with 'Unknown'
if 'crop_type' in df.columns:
    df['crop_type'] = df['crop_type'].fillna('Unknown')

# Fill date with a placeholder
if 'date' in df.columns:
    df['date'] = df['date'].fillna('Not Available')

# Null count after cleaning
print("\nNull values AFTER cleaning:")
print(df.isnull().sum())

# Save cleaned dataset as parquet
df.to_parquet(
    "data/processed/02_cleaned.parquet",
    index=False
)

# Save sample cleaned data
sample = df.head(50)

sample.to_csv(
    "data/processed/sample_cleaned_data.csv",
    index=False
)

print("\nCleaning completed successfully!")
print("Saved:")
print("- data/processed/02_cleaned.parquet")
print("- data/processed/sample_cleaned_data.csv")