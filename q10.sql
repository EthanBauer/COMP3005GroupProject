SELECT player, COUNT(events_dribbledpass.event_id) AS passed_dribbles
FROM events_dribbledpass
JOIN events ON events_dribbledpass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
-- WHERE season = '2020/2021' AND competition = 'La Liga'
WHERE season = '2020/2021' AND competition_id = 11
GROUP BY player, player_id
HAVING COUNT(events_dribbledpass.event_id) > 0
-- ORDER BY passed_dribbles ASC;
ORDER BY passed_dribbles ASC, player ASC;
