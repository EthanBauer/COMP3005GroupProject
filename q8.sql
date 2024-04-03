SELECT team, COUNT(pass_events.event_id) AS through_ball_count
FROM pass_events 
JOIN events ON pass_events.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season = '2020/2021' AND competition_id = 11 AND technique_id = 108
GROUP BY team
HAVING COUNT(pass_events.event_id) > 0
ORDER BY through_ball_count DESC;
