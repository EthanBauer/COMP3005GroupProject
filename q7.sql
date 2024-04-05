SELECT player, COUNT(events_pass.event_id) AS through_ball_count
FROM events_pass 
JOIN events ON events_pass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season = '2020/2021' AND competition_id = '11' AND technique_id = 108
-- WHERE season = '2020/2021' AND competition_id = 'La Liga' AND technique_id = 108
GROUP BY player, player_id
HAVING COUNT(events_pass.event_id) > 0
ORDER BY through_ball_count DESC;
