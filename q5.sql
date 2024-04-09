SELECT players.player_name,COUNT(events_pass.event_id) AS intended_recipient_count
FROM events_pass
JOIN events ON events_pass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
JOIN players ON events_pass.player_id = players.player_id
WHERE matches.season = '2003/2004' AND matches.competition_id = 2
GROUP BY players.player_id, players.player_name
HAVING COUNT(events_pass.event_id) > 0
ORDER BY intended_recipient_count DESC;