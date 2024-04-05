CREATE TABLE IF NOT EXISTS events_shot (
	event_id VARCHAR(50) PRIMARY KEY,
	team VARCHAR(40),
	team_id SMALLINT,
	player VARCHAR(60),
	player_id INT,
	xg_score NUMERIC(10, 9),
	first_time BOOLEAN
);