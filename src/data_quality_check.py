import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("database/nonprofit_crm.db")
OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

conn = sqlite3.connect(DB_PATH)

query = """
SELECT
    p.prospect_id,
    p.donor_id,
    d.first_name,
    d.last_name,
    d.email,
    p.assigned_fundraiser,
    p.giving_capacity,
    p.research_status,
    p.last_research_date,
    CASE
        WHEN d.email IS NULL OR d.email = '' THEN 'Missing donor email'
        WHEN p.assigned_fundraiser IS NULL OR p.assigned_fundraiser = '' THEN 'Missing assigned fundraiser'
        WHEN p.giving_capacity IS NULL THEN 'Missing giving capacity'
        WHEN p.last_research_date IS NULL OR p.last_research_date = '' THEN 'Missing last research date'
        ELSE 'Complete'
    END AS data_quality_issue
FROM prospects p
JOIN donors d
    ON p.donor_id = d.donor_id
WHERE 
    d.email IS NULL OR d.email = ''
    OR p.assigned_fundraiser IS NULL OR p.assigned_fundraiser = ''
    OR p.giving_capacity IS NULL
    OR p.last_research_date IS NULL OR p.last_research_date = '';
"""

issues = pd.read_sql_query(query, conn)

issues.to_csv(OUTPUT_DIR / "prospect_data_quality_issues.csv", index=False)

conn.close()

print("Data quality report generated:")
print(issues)