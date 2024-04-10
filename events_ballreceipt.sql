CREATE TABLE events_ballreceipt(
	event_id VARCHAR(50) PRIMARY KEY,
	team VARCHAR(40),
	team_id SMALLINT,
	player VARCHAR(60),
	player_id INT,
	incomplete BOOLEAN
);