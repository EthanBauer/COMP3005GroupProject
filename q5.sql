SELECT recipient ,COUNT(events_pass.event_id) AS intended_recipient_count
FROM events_pass
JOIN events ON events_pass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE matches.season_id = 44 AND matches.competition_id = 2 AND recipient IS NOT null 
GROUP BY recipient_id, recipient
HAVING COUNT(events_pass.event_id) > 0
ORDER BY intended_recipient_count DESC;