SELECT team,COUNT(events_shot.event_id) AS team_shot_count
FROM events_shot
JOIN events ON events_shot.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE matches.season_id = 44 AND matches.competition_id = 2
GROUP BY events_shot.team, events_shot.team_id
HAVING COUNT(events_shot.event_id) > 0
ORDER BY team_shot_count DESC;