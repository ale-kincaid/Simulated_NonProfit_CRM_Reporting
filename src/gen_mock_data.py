import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

donors = pd.DataFrame([
    {
        "donor_id": "D001",
        "first_name": "Maria",
        "last_name": "Johnson",
        "email": "maria.johnson@email.com",
        "city": "Indianapolis",
        "state": "IN",
        "donor_type": "Individual",
        "created_date": "2024-01-12",
    },
    {
        "donor_id": "D002",
        "first_name": "Smith Family Foundation",
        "last_name": "",
        "email": "contact@smithfoundation.org",
        "city": "Carmel",
        "state": "IN",
        "donor_type": "Foundation",
        "created_date": "2024-02-20",
    },
    {
        "donor_id": "D003",
        "first_name": "David",
        "last_name": "Lee",
        "email": "david.lee@email.com",
        "city": "Bloomington",
        "state": "IN",
        "donor_type": "Individual",
        "created_date": "2024-03-05",
    },
    {
        "donor_id": "D004",
        "first_name": "Angela",
        "last_name": "Rivera",
        "email": "",
        "city": "Fishers",
        "state": "IN",
        "donor_type": "Individual",
        "created_date": "2024-05-17",
    },
    {
        "donor_id": "D005", 
        "first_name": "Hasan", 
        "last_name": "Piker", 
        "email": "hpiker@gmail.com", 
        "city": "Los Angeles", 
        "state": "California", 
        "donor_type": "Individual", 
        "created_date": "2025-06-20"
    },
    {
    "donor_id": "D006", 
        "first_name": "The Yard", 
        "last_name": "", 
        "email": "yard@gmail.com", 
        "city": "Los Angeles", 
        "state": "California", 
        "donor_type": "Foundation", 
        "created_date": "2025-01-01"
    }
])

gifts = pd.DataFrame([
    {"gift_id": "G001", "donor_id": "D001", "campaign_id": "C001", "gift_date": "2025-01-15", "amount": 250.00, "gift_type": "Credit Card"},
    {"gift_id": "G002", "donor_id": "D002", "campaign_id": "C002", "gift_date": "2025-02-10", "amount": 5000.00, "gift_type": "Check"},
    {"gift_id": "G003", "donor_id": "D003", "campaign_id": "C001", "gift_date": "2025-03-01", "amount": 100.00, "gift_type": "Credit Card"},
    {"gift_id": "G004", "donor_id": "D001", "campaign_id": "C003", "gift_date": "2025-04-12", "amount": 500.00, "gift_type": "ACH"},
    {"gift_id": "G005", "donor_id": "D005", "campaign_id": "C003", "gift_date": "2025-08-09", "amount": 1000.00, "gift_type": "Credit Card"},
    {"gift_id": "G006", "donor_id": "D006", "campaign_id": "C002", "gift_date": "2025-10-31", "amount": 10000.00, "gift_type": "ACH"},
])

prospects = pd.DataFrame([
    {"prospect_id": "P001", "donor_id": "D001", "assigned_fundraiser": "Sarah Miller", "giving_capacity": 1000, "research_status": "Complete", "last_research_date": "2025-04-12", "notes": "Interested in pediatric research"},
    {"prospect_id": "P002", "donor_id": "D002", "assigned_fundraiser": "James Carter", "giving_capacity": 10000, "research_status": "In Progress", "last_research_date": "2025-04-20", "notes": "Foundation giving history identified"},
    {"prospect_id": "P003", "donor_id": "D003", "assigned_fundraiser": "Sarah Miller", "giving_capacity": None, "research_status": "Missing Info", "last_research_date": "", "notes": "Needs employer and capacity research"},
    {"prospect_id": "P004", "donor_id": "D004", "assigned_fundraiser": "", "giving_capacity": None, "research_status": "Missing Info", "last_research_date": "", "notes": "Missing email and assigned fundraiser"},
    {"prospect_id": "P005", "donor_id": "D005", "assigned_fundraiser": "Jim Carrey", "giving_capacity": 5000, "research_status": "Complete", "last_research_date": "2025-07-03", "notes": "Interested in laughter as medicine"},
    {"prospect_id": "P006", "donor_id": "D006", "assigned_fundraiser": "", "giving_capacity": 1000, "research_status": "In Progress", "last_research_date": "2025-01-21", "notes": "Needs assigned fundraiser"},

])

events = pd.DataFrame([
    {"event_id": "E001", "event_name": "Annual Gala", "donor_id": "D001", "event_date": "2025-05-10", "attended": "Yes"},
    {"event_id": "E001", "event_name": "Annual Gala", "donor_id": "D002", "event_date": "2025-05-10", "attended": "Yes"},
    {"event_id": "E002", "event_name": "Donor Breakfast", "donor_id": "D003", "event_date": "2025-06-12", "attended": "No"},
    {"event_id": "E002", "event_name": "Donor Breakfast", "donor_id": "D004", "event_date": "2025-06-12", "attended": "Yes"},
    {"event_id": "E003", "event_name": "Donor Dinner", "donor_id": "D005", "event_date": "2026-03-12", "attended": "Yes"},
    {"event_id": "E002", "event_name": "Donor Dinner", "donor_id": "D006", "event_date": "2026-03-12", "attended": "No"},
])

interactions = pd.DataFrame([
    {"interaction_id": "I001", "donor_id": "D001", "fundraiser": "Sarah Miller", "interaction_date": "2025-04-15", "interaction_type": "Call", "summary": "Discussed interest in children's healthcare"},
    {"interaction_id": "I002", "donor_id": "D002", "fundraiser": "James Carter", "interaction_date": "2025-04-25", "interaction_type": "Email", "summary": "Sent foundation sponsorship information"},
    {"interaction_id": "I003", "donor_id": "D003", "fundraiser": "Sarah Miller", "interaction_date": "2025-05-01", "interaction_type": "Meeting", "summary": "Follow-up needed"},
    {"interaction_id": "I005", "donor_id": "D005", "fundraiser": "Jim Carrey", "interaction_date": "2025-05-01", "interaction_type": "Call", "summary": "Discussed research interest"}
])

donors.to_csv(DATA_DIR / "donors.csv", index=False)
gifts.to_csv(DATA_DIR / "gifts.csv", index=False)
prospects.to_csv(DATA_DIR / "prospects.csv", index=False)
events.to_csv(DATA_DIR / "events.csv", index=False)
interactions.to_csv(DATA_DIR / "interactions.csv", index=False)

print("Mock CRM data generated successfully.")