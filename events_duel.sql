CREATE TABLE IF NOT EXISTS events_duel (
	event_id VARCHAR(50) PRIMARY KEY,
	type VARCHAR(20),
	type_id SMALLINT,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);