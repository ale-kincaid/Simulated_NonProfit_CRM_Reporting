# Data Dictionary

## donors

| Column | Description |
|---|---|
| donor_id | Unique donor identifier |
| first_name | Donor first name or organization name |
| last_name | Donor last name |
| email | Donor email address |
| city | Donor city |
| state | Donor state |
| donor_type | Individual, Foundation, Corporate, etc. |
| created_date | Date donor record was created |

## gifts

| Column | Description |
|---|---|
| gift_id | Unique gift transaction ID |
| donor_id | Links gift to donor |
| campaign_id | Campaign associated with gift |
| gift_date | Date gift was received |
| amount | Gift amount |
| gift_type | Payment method |

## prospects

| Column | Description |
|---|---|
| prospect_id | Unique prospect record ID |
| donor_id | Links prospect to donor |
| assigned_fundraiser | Fundraiser responsible for relationship |
| giving_capacity | Estimated giving capacity |
| research_status | Status of prospect research |
| last_research_date | Date research was last updated |
| notes | Prospect research notes |