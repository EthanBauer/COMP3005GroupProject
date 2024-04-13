CREATE TABLE IF NOT EXISTS events_block (
	event_id VARCHAR(50) PRIMARY KEY,
	deflection BOOLEAN,
	offensive BOOLEAN,
	save_block BOOLEAN,
	counterpress BOOLEAN
);