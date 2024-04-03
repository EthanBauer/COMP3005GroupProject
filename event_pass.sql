CREATE TABLE pass_events (
	event_id VARCHAR(50) PRIMARY KEY,
	team VARCHAR(20),
	team_id SMALLINT,
	player VARCHAR(40),
	player_id INT,
	recipient VARCHAR(40),
	recipient_id INT,
	type VARCHAR(16),
	type_id SMALLINT,
	end_loc_x numeric(5,2),
	end_loc_y numeric(5,2),
	outcome_id VARCHAR(3),
	outcome VARCHAR(20)
);