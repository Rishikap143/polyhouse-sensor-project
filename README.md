# Polyhouse Sensor Project

## Objective
Load polyhouse sensor CSV files, identify and handle missing values, and generate a cleaned dataset suitable for analysis and machine learning.

## Project Structure


polyhouse-sensor-project/
│
├── data/
│   ├── raw/
│   │   ├── climate_data.csv
│   │   ├── polyhouse_sensor.csv
│   │   └── yield_data.csv
│   │
│   └── processed/
│       ├── 02_cleaned.parquet
│       └── sample_cleaned_data.csv
│
├── docs/
│   └── cleaning_log.md
│
├── src/
│   ├── ingest_data.py
│   └── clean_data.py
│
└── README.md


## Features

- Loads raw sensor and climate datasets.
- Audits missing values.
- Cleans and preprocesses data.
- Generates cleaned output in Parquet format.
- Produces a sample cleaned dataset.
- Documents all cleaning decisions.

## Data Cleaning Strategy

- Temperature: Missing values imputed using median.
- Humidity: Missing values imputed using median.
- CO₂: Missing values imputed using median.
- Yield: Rows with missing target values removed.

The cleaning rationale is documented in docs/cleaning_log.md.

## Output Files

### Cleaned Dataset

data/processed/02_cleaned.parquet


### Sample Dataset

data/processed/sample_cleaned_data.csv


### Cleaning Log

docs/cleaning_log.md


## How to Run

### Data Ingestion

bash
python src/ingest_data.py


### Data Cleaning

bash
python src/clean_data.py


## Technologies Used

- Python
- Pandas
- NumPy
- Parquet
- Git
- GitHub
