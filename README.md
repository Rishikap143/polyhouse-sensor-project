\# Polyhouse Sensor Project



\## Objective

Load polyhouse sensor CSV files, identify and handle missing values, and generate a cleaned dataset suitable for analysis and machine learning.



\## Project Structure





polyhouse-sensor-project/

│

├── data/

│   ├── raw/

│   │   ├── climate\_data.csv

│   │   ├── polyhouse\_sensor.csv

│   │   └── yield\_data.csv

│   │

│   └── processed/

│       ├── 02\_cleaned.parquet

│       └── sample\_cleaned\_data.csv

│

├── docs/

│   └── cleaning\_log.md

│

├── src/

│   ├── ingest\_data.py

│   └── clean\_data.py

│

└── README.md





\## Features



\- Loads raw sensor and climate datasets.

\- Audits missing values.

\- Cleans and preprocesses data.

\- Generates cleaned output in Parquet format.

\- Produces a sample cleaned dataset.

\- Documents all cleaning decisions.



\## Data Cleaning Strategy



\- Temperature: Missing values imputed using median.

\- Humidity: Missing values imputed using median.

\- CO₂: Missing values imputed using median.

\- Yield: Rows with missing target values removed.



The cleaning rationale is documented in docs/cleaning\_log.md.



\## Output Files



\### Cleaned Dataset



data/processed/02\_cleaned.parquet





\### Sample Dataset



data/processed/sample\_cleaned\_data.csv





\### Cleaning Log



docs/cleaning\_log.md





\## How to Run



\### Data Ingestion



bash

python src/ingest\_data.py





\### Data Cleaning



bash

python src/clean\_data.py





\## Technologies Used



\- Python

\- Pandas

\- NumPy

\- Parquet

\- Git

\- GitHub



