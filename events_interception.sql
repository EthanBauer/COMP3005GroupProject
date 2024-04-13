CREATE TABLE IF NOT EXISTS events_interception (
	event_id VARCHAR(50) PRIMARY KEY,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);