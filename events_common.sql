CREATE TABLE IF NOT EXISTS events (
	event_id VARCHAR(50) PRIMARY KEY,
	team VARCHAR(40),
	team_id SMALLINT,
	player VARCHAR(60),
	player_id INT,
	index SMALLINT,
	period SMALLINT,
	timestamp VARCHAR(16),
	minute VARCHAR(3),
	second VARCHAR(3),
	type_id SMALLINT,
	type_name VARCHAR(20),
	match_id VARCHAR(10)
)