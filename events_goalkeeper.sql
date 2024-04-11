CREATE TABLE IF NOT EXISTS events_goalkeeper (
	event_id VARCHAR(50) PRIMARY KEY,
	position VARCHAR(40),
	position_id SMALLINT,
	technique VARCHAR(40),
	technique_id SMALLINT,
	body_part VARCHAR(40),
	body_part_id SMALLINT,
	type VARCHAR(40),
	type_id SMALLINT,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);