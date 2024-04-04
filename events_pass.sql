CREATE TABLE IF NOT EXISTS events_pass (
	event_id VARCHAR(50) PRIMARY KEY,
	team VARCHAR(40),
	team_id SMALLINT,
	player VARCHAR(60),
	player_id INT,
	recipient VARCHAR(60),
	recipient_id INT,
	type VARCHAR(16),
	type_id SMALLINT,
	technique VARCHAR(20),
	technique_id SMALLINT,
	end_loc_x numeric(5,2),
	end_loc_y numeric(5,2),
	outcome_id VARCHAR(3),
	outcome VARCHAR(40)
);