SELECT team, COUNT(*) AS num_passes
FROM events_pass
JOIN events ON events_pass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season = '2020/2021'
GROUP BY team
HAVING COUNT(*) >= 1
ORDER BY num_passes DESC