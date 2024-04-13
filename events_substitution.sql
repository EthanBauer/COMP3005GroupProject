CREATE TABLE IF NOT EXISTS events_substitution (
	event_id VARCHAR(50) PRIMARY KEY,
	replacement VARCHAR(60),
	replacement_id INT,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);
