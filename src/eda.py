from pathlib import Path
import pandas as pd

<<<<<<< HEAD
df = pd.read_csv(
    "data/processed/sample_cleaned_data.csv",
    sep="\t"
)
print(df.columns)
=======
df = pd.read_parquet("data/processed/02_cleaned.parquet")

>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
print("\nDATA INFO")
print(df.info())

print("\nSUMMARY STATISTICS")
print(df.describe())

print("\nCOLUMNS")
print(df.columns)

print("\nDATE RANGE")
<<<<<<< HEAD
print("Start Date:", df['timestamp'].min())
print("End Date:", df['timestamp'].max())
print("Total Observations:", len(df))

# Generate data quality report
summary = df[["temperature", "humidity", "CO2", "yield"]].describe().T
=======
print("Start Date:", df['date'].min())
print("End Date:", df['date'].max())
print("Total Observations:", len(df))

# Generate data quality report
summary = df[["temperature", "humidity", "co2", "yield_kg"]].describe().T
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
summary["cv"] = summary["std"] / summary["mean"]

report = []
report.append("# Polyhouse Data Quality Report\n")
report.append(f"Rows: {len(df)}\n")
<<<<<<< HEAD
report.append(f"Date range: {df['timestamp'].min()} → {df['timestamp'].max()}\n\n")
=======
report.append(f"Date range: {df['date'].min()} → {df['date'].max()}\n\n")
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
report.append(summary.to_string())

Path("reports").mkdir(exist_ok=True)

Path("reports/data_quality.md").write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("Data quality report generated successfully.")
import os
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("reports/figures", exist_ok=True)

# Correlation Heatmap
plt.figure(figsize=(8, 6))
<<<<<<< HEAD
corr = df[['temperature', 'humidity', 'CO2', 'yield']].corr()
=======
corr = df[['temperature', 'humidity', 'co2', 'yield_kg']].corr()
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("reports/figures/correlation_heatmap.png")
plt.close()

# Humidity vs Yield
plt.figure(figsize=(8, 6))
<<<<<<< HEAD
plt.scatter(df['humidity'], df['yield'])
=======
plt.scatter(df['humidity'], df['yield_kg'])
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
plt.xlabel("Humidity (%)")
plt.ylabel("Yield (kg)")
plt.title("Humidity vs Yield")
plt.savefig("reports/figures/humidity_vs_yield.png")
plt.close()

# CO₂ vs Yield
plt.figure(figsize=(8, 6))
<<<<<<< HEAD
plt.scatter(df['CO2'], df['yield'])
=======
plt.scatter(df['co2'], df['yield_kg'])
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
plt.xlabel("CO₂ (ppm)")
plt.ylabel("Yield (kg)")
plt.title("CO₂ vs Yield")
plt.savefig("reports/figures/co2_vs_yield.png")
plt.close()

# Temperature vs Yield
plt.figure(figsize=(8, 6))
<<<<<<< HEAD
plt.scatter(df['temperature'], df['yield'])
=======
plt.scatter(df['temperature'], df['yield_kg'])
>>>>>>> 7f05e11df5fcc7592a22e75b856967e373f5725a
plt.xlabel("Temperature (°C)")
plt.ylabel("Yield (kg)")
plt.title("Temperature vs Yield")
plt.savefig("reports/figures/temperature_vs_yield.png")
plt.close()

print("All figures generated successfully.")