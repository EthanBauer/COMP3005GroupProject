CREATE TABLE IF NOT EXISTS lineups (
    match_id INTEGER,
    team_id INTEGER,
    team_name TEXT,
    player_id INTEGER,
    player_name TEXT,
	PRIMARY KEY (match_id, player_id)
);