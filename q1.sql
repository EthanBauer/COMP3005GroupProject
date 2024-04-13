SELECT player, AVG(xg_score) AS average_xg_score
FROM events_shot 
JOIN events ON events_shot.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
-- WHERE season = '2020/2021' AND competition = 'La Liga'
WHERE season_id = 90 AND competition_id = 11
GROUP BY player, player_id
HAVING AVG(xg_score) > 0
ORDER BY AVG(xg_score) DESC;

--  2018/2019 4
--  2019/2020 42
--  2020/2021 90
--  2003/2004 44