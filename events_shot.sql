CREATE TABLE IF NOT EXISTS events_shot (
	event_id VARCHAR(50) PRIMARY KEY,
	xg_score NUMERIC(10, 9),
	first_time BOOLEAN,
	end_location numeric[],
	technique_id INTEGER,
	technique_label VARCHAR(50),
	body_part_id INTEGER,
	body_part_label VARCHAR(50),
	type_id INTEGER,
	type_label VARCHAR(50),
	outcome_id INTEGER,
	outcome_label VARCHAR(50)
);