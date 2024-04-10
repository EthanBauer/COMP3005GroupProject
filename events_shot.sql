CREATE TABLE IF NOT EXISTS events_shot (
	event_id VARCHAR(50) PRIMARY KEY,
	xg_score NUMERIC(10, 9),
	first_time BOOLEAN
);