CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    match_date DATE,
    kick_off TIME,
    competition_id INTEGER,
    season_id INTEGER,
    home_team_id INTEGER,
    home_manager_id INTEGER,
    away_team_id INTEGER,
    away_manager_id INTEGER,
    home_score INTEGER,
    away_score INTEGER,
    match_status VARCHAR(20),
    match_status_360 VARCHAR(20),
    last_updated TIMESTAMP,
    last_updated_360 TIMESTAMP,
    match_week INTEGER,
    competition_stage_id INTEGER,
    stadium_id INTEGER,
    referee_id INTEGER
);