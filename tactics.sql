CREATE TABLE IF NOT EXIST tactics (
    id SERIAL PRIMARY KEY,
    formation INT,
    player_id INT[],
    player_name TEXT[],
    position_id INT[],
    position_name TEXT[],
    jersey_number INT[]
);