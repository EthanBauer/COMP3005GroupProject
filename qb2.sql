SELECT team, COUNT(*) AS num_passes
FROM events_pass
JOIN events ON events_pass.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE season_id = 90 AND competition_id = 11 
AND ((end_loc_x >=0 AND end_loc_x <=18 ) or (end_loc_x >=102 AND end_loc_x <=120 ))
AND (end_loc_y >=18 AND end_loc_y <=62 ) 
GROUP BY team
HAVING COUNT(*) >= 1
ORDER BY num_passes DESC