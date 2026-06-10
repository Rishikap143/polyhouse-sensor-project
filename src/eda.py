from pathlib import Path
import pandas as pd

df = pd.read_csv(
    "data/processed/sample_cleaned_data.csv",
    sep="\t"
)
print(df.columns)
print("\nDATA INFO")
print(df.info())

print("\nSUMMARY STATISTICS")
print(df.describe())

print("\nCOLUMNS")
print(df.columns)

print("\nDATE RANGE")
print("Start Date:", df['timestamp'].min())
print("End Date:", df['timestamp'].max())
print("Total Observations:", len(df))

# Generate data quality report
summary = df[["temperature", "humidity", "CO2", "yield"]].describe().T
summary["cv"] = summary["std"] / summary["mean"]

report = []
report.append("# Polyhouse Data Quality Report\n")
report.append(f"Rows: {len(df)}\n")
report.append(f"Date range: {df['timestamp'].min()} → {df['timestamp'].max()}\n\n")
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
corr = df[['temperature', 'humidity', 'CO2', 'yield']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("reports/figures/correlation_heatmap.png")
plt.close()

# Humidity vs Yield
plt.figure(figsize=(8, 6))
plt.scatter(df['humidity'], df['yield'])
plt.xlabel("Humidity (%)")
plt.ylabel("Yield (kg)")
plt.title("Humidity vs Yield")
plt.savefig("reports/figures/humidity_vs_yield.png")
plt.close()

# CO₂ vs Yield
plt.figure(figsize=(8, 6))
plt.scatter(df['CO2'], df['yield'])
plt.xlabel("CO₂ (ppm)")
plt.ylabel("Yield (kg)")
plt.title("CO₂ vs Yield")
plt.savefig("reports/figures/co2_vs_yield.png")
plt.close()

# Temperature vs Yield
plt.figure(figsize=(8, 6))
plt.scatter(df['temperature'], df['yield'])
plt.xlabel("Temperature (°C)")
plt.ylabel("Yield (kg)")
plt.title("Temperature vs Yield")
plt.savefig("reports/figures/temperature_vs_yield.png")
plt.close()

print("All figures generated successfully.")