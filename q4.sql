SELECT team, COUNT(*) AS num_passes
FROM events_pass
JOIN events ON events_pass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season_id = 90 AND competition_id = 11 
GROUP BY team
HAVING COUNT(*) >= 1
ORDER BY num_passes DESC


--  2018/2019 4
--  2019/2020 42
--  2020/2021 90
--  2003/2004 44