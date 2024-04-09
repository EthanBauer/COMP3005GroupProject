CREATE INDEX IF NOT EXISTS events_shot_index ON events_shot (event_id);
CREATE INDEX IF NOT EXISTS events_pass_index ON events_pass (event_id);
CREATE INDEX IF NOT EXISTS events_index ON events (match_id);
CREATE INDEX IF NOT EXISTS matches_index ON matches (season_id, competition_id);
CREATE INDEX IF NOT EXISTS players_index ON players (player_id);
CREATE INDEX IF NOT EXISTS lineups_index ON lineups (match_id, player_id, team_id);