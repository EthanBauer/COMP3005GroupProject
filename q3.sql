SELECT player, COUNT(events.event_id) AS first_shot_count
FROM events_shot 
JOIN events ON events_shot.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season_id in  (90, 42, 4)  AND competition_id = 11 AND first_time = TRUE
GROUP BY player, player_id
HAVING COUNT(events.event_id)>0
ORDER BY COUNT(events.event_id) DESC;