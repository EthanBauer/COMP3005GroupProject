CREATE TABLE startingxi (
    event_id VARCHAR(50) PRIMARY KEY,
    period INTEGER,
    timestamp TIME,
    minute INTEGER,
    second INTEGER,
    possession INTEGER,
    possession_team_id INTEGER,
    possession_team_name VARCHAR(100),
    play_pattern_id INTEGER,
    play_pattern_name VARCHAR(100),
    team_id INTEGER,
    team_name VARCHAR(100),
    duration FLOAT,
    tactics_formation INTEGER
);