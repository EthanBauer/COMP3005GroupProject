CREATE TABLE IF NOT EXISTS events_clearance (
	event_id VARCHAR(50) PRIMARY KEY,
	aerial_won BOOLEAN,
	head BOOLEAN,
	left_foot BOOLEAN,
	right_foot BOOLEAN,
	other BOOLEAN
);
