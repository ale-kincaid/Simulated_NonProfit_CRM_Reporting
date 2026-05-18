import sqlite3
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data") 
DB_PATH = Path("database/nonprofit_crm.db")

DB_PATH.parent.mkdir(exist_ok=True) 
conn = sqlite3.connect(DB_PATH)

tables = { 
          "donors": "donors.csv", 
          "gifts": "gifts.csv", 
          "prospects": "prospects.csv", 
          "events": "events.csv", 
          "interactions": "interactions.csv"
}

for table_name, csv_file in tables.items(): 
    df = pd.read_csv(DATA_DIR / csv_file)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {table_name} table with {len(df)} rows.")

conn.close() 
print("Database created")