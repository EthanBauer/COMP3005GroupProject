CREATE TABLE IF NOT EXISTS tactics (
    event_id VARCHAR(50) PRIMARY KEY,
    formation INT,
    player_id INT[],
    player_name TEXT[],
    position_id INT[],
    position_name TEXT[],
    jersey_number INT[]
);