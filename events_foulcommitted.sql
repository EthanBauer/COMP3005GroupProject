CREATE TABLE IF NOT EXISTS events_foulcommitted (
	event_id VARCHAR(50) PRIMARY KEY,
	counterpress BOOLEAN,
	offensive BOOLEAN,
	advantage BOOLEAN,
	penalty BOOLEAN,
	type VARCHAR(20),
	type_id SMALLINT,
	card VARCHAR(40),
	card_id SMALLINT
);