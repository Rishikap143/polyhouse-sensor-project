# Cleaning Log

## Dataset Audit

### Null Counts Before Cleaning

| Column          | Null Count |
| --------------- | ---------- |
| timestamp       | 10         |
| temperature     | 11         |
| humidity        | 11         |
| light_intensity | 11         |
| co2             | 11         |
| soil_moisture   | 21         |
| date            | 30         |
| crop_type       | 30         |
| yield_kg        | 30         |

## Cleaning Actions Performed

### Temperature

* Missing values filled using median value.
* Reason: Temperature changes gradually in a polyhouse and median preserves the overall trend.

### Humidity

* Missing values filled using median value.
* Reason: Humidity readings are continuous environmental measurements.

### Soil Moisture

* Missing values filled using median value.
* Reason: Prevents loss of important crop-condition data.

### Light Intensity

* Missing values filled using median value.
* Reason: Missing readings are often caused by temporary sensor issues.

### CO₂

* Missing values filled using median value.
* Reason: Environmental values remain relatively stable over short periods.

### Yield Data

* Missing yield values filled using median value.

### Timestamp

* Rows with missing timestamps removed.
* Reason: Time information is essential for sensor data analysis.

### Crop Type

* Missing values replaced with "Unknown".

### Date

* Missing values replaced with "Not Available".

## Null Counts After Cleaning

| Column          | Null Count |
| --------------- | ---------- |
| timestamp       | 0          |
| temperature     | 0          |
| humidity        | 0          |
| light_intensity | 0          |
| co2             | 0          |
| soil_moisture   | 0          |
| date            | 0          |
| crop_type       | 0          |
| yield_kg        | 0          |

## Output Files

* data/processed/02_cleaned.parquet
* data/processed/sample_cleaned_data.csv
