CREATE TABLE events (
	event_id VARCHAR(50) PRIMARY KEY,
	index SMALLINT,
	period SMALLINT,
	timestamp VARCHAR(16),
	minute VARCHAR(3),
	second VARCHAR(3),
	type_id VARCHAR(3),
	type_name VARCHAR(20)
)