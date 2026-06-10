\# Cleaning Log



\## Null Counts Before Cleaning



\* temperature: 1

\* humidity: 1

\* soil\_moisture: 1

\* light\_intensity: 1

\* co2: 1



\## Cleaning Actions



\* Filled missing sensor values using forward-fill and backward-fill.

\* Filled missing crop\_type values with "Tomato".

\* Removed duplicate timestamps.

\* Removed rows with missing yield values if any.



\## Null Counts After Cleaning



\* All columns: 0 missing values



\## Output Files



\* `01\_combined.csv`

\* `02\_cleaned.parquet`

\* `sample\_cleaned\_data.csv`



\*\*Dataset Summary\*\*



\* Original rows: 50

\* Cleaned rows: 50



