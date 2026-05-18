SELECT 
    campaign_id,
    COUNT(gift_id) AS number_of_gifts,
    SUM(amount) AS total_raised,
    AVG(amount) AS average_gift
FROM gifts
GROUP BY campaign_id
ORDER BY total_raised DESC;

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

SELECT
    p.prospect_id,
    p.donor_id,
    d.first_name,
    d.last_name,
    d.email,
    p.assigned_fundraiser,
    p.giving_capacity,
    p.research_status,
    p.last_research_date
FROM prospects p
JOIN donors d
    ON p.donor_id = d.donor_id
WHERE 
    p.giving_capacity IS NULL
    OR p.assigned_fundraiser = ''
    OR p.last_research_date = ''
    OR d.email = '';

SELECT
    fundraiser,
    COUNT(interaction_id) AS total_interactions,
    MIN(interaction_date) AS first_interaction,
    MAX(interaction_date) AS most_recent_interaction
FROM interactions
GROUP BY fundraiser
ORDER BY total_interactions DESC;

SELECT
    e.event_name,
    COUNT(DISTINCT e.donor_id) AS total_invited_or_recorded,
    SUM(CASE WHEN e.attended = 'Yes' THEN 1 ELSE 0 END) AS total_attended,
    COALESCE(SUM(g.amount), 0) AS total_donations_from_attendees
FROM events e
LEFT JOIN gifts g
    ON e.donor_id = g.donor_id
GROUP BY e.event_name
ORDER BY total_donations_from_attendees DESC;