SELECT player, AVG(xg_score) AS average_xg_score
FROM events_shot 
JOIN events ON events_shot.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season = '2020/2021' AND competition = 'La Liga'
GROUP BY player, player_id
HAVING AVG(xg_score) > 0
ORDER BY AVG(xg_score) DESC;