CREATE INDEX IF NOT EXISTS events_shot_index ON events_shot (event_id);
CREATE INDEX IF NOT EXISTS events_pass_index ON events_pass (event_id);
CREATE INDEX IF NOT EXISTS events_pass_index2 ON events_pass (recipient_id);
CREATE INDEX IF NOT EXISTS events_pass_index3 ON events_pass (recipient);
CREATE INDEX IF NOT EXISTS events_pass_index4 ON events_pass (technique_id);

CREATE INDEX IF NOT EXISTS events_index ON events (match_id);
CREATE INDEX IF NOT EXISTS events_index2 ON events (player_id);
CREATE INDEX IF NOT EXISTS events_index3 ON events (player);
CREATE INDEX IF NOT EXISTS events_index4 ON events (team_id);
CREATE INDEX IF NOT EXISTS events_index5 ON events (team);

CREATE INDEX IF NOT EXISTS events_dribble_index1 ON events_dribble (event_id);

CREATE INDEX IF NOT EXISTS events_dribbledpass_index1 ON events_dribbledpass (event_id);

CREATE INDEX IF NOT EXISTS matches_index ON matches (season_id, competition_id);
CREATE INDEX IF NOT EXISTS matches_index2 ON matches (season_id);
CREATE INDEX IF NOT EXISTS matches_index3 ON matches (competition_id);
CREATE INDEX IF NOT EXISTS matches_index4 ON matches (match_id);

CREATE INDEX IF NOT EXISTS players_index ON players (player_id);
CREATE INDEX IF NOT EXISTS lineups_index ON lineups (match_id, player_id, team_id);

CREATE INDEX IF NOT EXISTS competitions_index1 ON competitions(competition_id);
CREATE INDEX IF NOT EXISTS competitions_index2 ON competitions(season_id);