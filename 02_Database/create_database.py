import sqlite3
import pandas as pd
import os

# Database Path
db_path = "02_Database/ev_analytics.db"

# Cleaned Data Folder
cleaned_folder = "03_Data_Preparation/Cleaned_Data"

# Connect Database
conn = sqlite3.connect(db_path)

files = {
    "electric_vehicles_spec_2025.csv": "vehicle_specs",
    "ev-charging-stations-india.csv": "charging_stations",
    "EV_Dataset (1).csv": "ev_sales",
    "global_ev_market_charging_infrastructure_2026.csv": "global_market"
}

for file, table in files.items():
    path = os.path.join(cleaned_folder, file)
    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"{table} imported successfully.")

conn.close()

print("\nDatabase created successfully.")