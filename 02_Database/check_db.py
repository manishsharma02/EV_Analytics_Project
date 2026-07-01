import sqlite3
conn = sqlite3.connect('ev_analytics.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

tables = ['cheapestelectriccars', 'electric_vehicle_charging', 'electriccardata_clean', 'evindia']
for t in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {t}")
    print(t, "->", cursor.fetchone()[0])

conn.close()

