-- goal: y = 36 - 44
--       z = 0 - 2.67

-- z = top down, so this will be split into 2 sections.
-- Therefore, 2.67/2 = SELECT 2.67/2 = 1.335. So, z values that are greater than 1.335 will be considered

-- y = left right, so this will be split into 3 equal sections.
-- Therefore, 44-36 = SELECT 44-36 = 8, 8.0/3 = SELECT 8.0/3 = 2.67. So, y values that are between:
--   36 -> (36 + 2.67) are considered left.
--   44 -> (44 - 2.67) are considered right.
  
-- SELECT 36 + 2.67 = 38.67
-- SELECT 44 - 2.67 = 41.33

-- Now, to confirm our math, 41.33 - 38.67 should equal roughly 2.67.
-- SELECT 41.33 - 38.67

WITH shot_on_goal as (
SELECT event_id, end_location FROM events_shot
WHERE end_location[3] IS NOT NULL AND end_location[3] >= 1.335)
SELECT events.player, COUNT(shot_on_goal.event_id) as shots_top_left_or_right FROM shot_on_goal
JOIN events ON shot_on_goal.event_id = events.event_id
JOIN matches ON events.match_id = matches.match_id
WHERE (matches.season_id = 90 AND matches.competition_id = 11) OR (matches.season_id = 4 AND matches.competition_id = 11)
OR (matches.season_id = 42 AND matches.competition_id = 11)
AND ((end_location[2] >= 36 AND end_location[2] < 38.67) OR (end_location[3] <= 44 AND end_location[3] >= 41.33))
GROUP BY events.player
HAVING COUNT(shot_on_goal.event_id) > 0
ORDER BY shots_top_left_or_right DESC