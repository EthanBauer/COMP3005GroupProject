CREATE TABLE events_5050 (
	event_id VARCHAR(50) PRIMARY KEY,
	team VARCHAR(40),
	team_id SMALLINT,
	player VARCHAR(60),
	player_id INT,
	outcome VARCHAR(40),
	outcome_id SMALLINT,
	counterpress BOOLEAN
);