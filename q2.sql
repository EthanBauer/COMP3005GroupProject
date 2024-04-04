SELECT player, COUNT(*) AS num_shots
FROM events_shot
JOIN events ON events_shot.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season = '2020/2021'
GROUP BY player, player_id
HAVING COUNT(*) >= 1
ORDER BY num_shots DESC