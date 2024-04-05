SELECT team, COUNT(events_pass.event_id) AS through_ball_count
FROM events_pass 
JOIN events ON events_pass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season = '2020/2021' AND competition_id = 11 AND technique_id = 108
-- GROUP BY team， team_id
GROUP BY team
HAVING COUNT(events_pass.event_id) > 0
ORDER BY through_ball_count DESC;
