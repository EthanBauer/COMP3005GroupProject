CREATE TABLE events_dribble (
	event_id VARCHAR(50) PRIMARY KEY,
	team VARCHAR(40),
	team_id SMALLINT,
	player VARCHAR(60),
	player_id INT,
	complete BOOLEAN,
    no_touch BOOLEAN,
    nutmeg BOOLEAN,
    overrun BOOLEAN
);