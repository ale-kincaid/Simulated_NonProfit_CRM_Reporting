import sqlite3
import pandas as pd
import streamlit as st
from pathlib import Path

DB_PATH = Path("database/nonprofit_crm.db")

st.set_page_config(
    page_title="Nonprofit CRM Reporting Dashboard",
    layout="wide"
)

st.title("Nonprofit CRM Reporting & Data Quality Dashboard")

conn = sqlite3.connect(DB_PATH)

donors = pd.read_sql_query("SELECT * FROM donors", conn)
gifts = pd.read_sql_query("SELECT * FROM gifts", conn)
prospects = pd.read_sql_query("SELECT * FROM prospects", conn)
events = pd.read_sql_query("SELECT * FROM events", conn)
interactions = pd.read_sql_query("SELECT * FROM interactions", conn)

total_raised = gifts["amount"].sum()
total_donors = donors["donor_id"].nunique()
total_prospects = prospects["prospect_id"].nunique()
total_interactions = interactions["interaction_id"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Raised", f"${total_raised:,.2f}")
col2.metric("Total Donors", total_donors)
col3.metric("Total Prospects", total_prospects)
col4.metric("Fundraiser Interactions", total_interactions)

st.divider()

st.header("Campaign Performance")

campaign_report = pd.read_sql_query("""
SELECT 
    campaign_id,
    COUNT(gift_id) AS number_of_gifts,
    SUM(amount) AS total_raised,
    AVG(amount) AS average_gift
FROM gifts
GROUP BY campaign_id
ORDER BY total_raised DESC;
""", conn)

st.dataframe(campaign_report, width="stretch")
st.bar_chart(campaign_report.set_index("campaign_id")["total_raised"])

st.header("Top Donors")

top_donors = pd.read_sql_query("""
SELECT
    d.donor_id,
    d.first_name,
    d.last_name,
    d.donor_type,
    SUM(g.amount) AS total_given
FROM donors d
JOIN gifts g
    ON d.donor_id = g.donor_id
GROUP BY
    d.donor_id,
    d.first_name,
    d.last_name,
    d.donor_type
ORDER BY total_given DESC;
""", conn)

st.dataframe(top_donors, width="stretch")

st.header("Prospect Data Quality Issues")

data_quality = pd.read_sql_query("""
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
""", conn)

st.dataframe(data_quality, width="stretch")

st.header("Fundraiser Activity")

fundraiser_activity = pd.read_sql_query("""
SELECT
    fundraiser,
    COUNT(interaction_id) AS total_interactions,
    MIN(interaction_date) AS first_interaction,
    MAX(interaction_date) AS most_recent_interaction
FROM interactions
GROUP BY fundraiser
ORDER BY total_interactions DESC;
""", conn)

st.dataframe(fundraiser_activity, width="stretch")

st.header("Event Attendance")

event_report = pd.read_sql_query("""
SELECT
    event_name,
    COUNT(DISTINCT donor_id) AS total_recorded,
    SUM(CASE WHEN attended = 'Yes' THEN 1 ELSE 0 END) AS total_attended
FROM events
GROUP BY event_name;
""", conn)

st.dataframe(event_report, width="stretch")

conn.close()