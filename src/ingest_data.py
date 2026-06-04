import pandas as pd
import glob

csv_files = glob.glob("data/raw/*.csv")

df_list = []

for file in csv_files:
    print(f"Reading {file}")
    df = pd.read_csv(file)
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

print("\nDataset Shape:", combined_df.shape)

combined_df.to_csv(
    "data/processed/01_combined.csv",
    index=False
)

print("Combined file saved successfully!")