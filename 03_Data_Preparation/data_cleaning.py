import pandas as pd
import os

# Project Paths
dataset_folder = "01_Dataset"
output_folder = "03_Data_Preparation/Cleaned_Data"

os.makedirs(output_folder, exist_ok=True)

files = [
    "electric_vehicles_spec_2025.csv",
    "ev-charging-stations-india.csv",
    "EV_Dataset (1).csv",
    "global_ev_market_charging_infrastructure_2026.csv"
]

for file in files:
    print("="*60)
    print("Processing:", file)

    path = os.path.join(dataset_folder, file)

    df = pd.read_csv(path)

    print("Rows :", df.shape[0])
    print("Columns :", df.shape[1])

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows :", df.duplicated().sum())

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove extra spaces from text columns
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip()

    output_path = os.path.join(output_folder, file)
    df.to_csv(output_path, index=False)

    print("Cleaned file saved :", output_path)

print("\nAll datasets cleaned successfully.")