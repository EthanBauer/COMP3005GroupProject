SELECT player, COUNT(events_dribble.event_id) AS completed_dribbles
FROM events_dribble
JOIN events ON events_dribble.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season in ('2018/2019', '2019/2020', '2020/2021') AND competition_id = 11
GROUP BY player, player_id
HAVING COUNT(events_dribble.event_id) > 0
ORDER BY completed_dribbles DESC;
