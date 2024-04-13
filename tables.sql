CREATE TABLE IF NOT EXISTS competitions (
    competition_id INTEGER,
    season_id INTEGER,
    country_name TEXT,
    competition_name TEXT,
    competition_gender TEXT,
    competition_youth BOOLEAN,
    competition_international BOOLEAN,
    season_name TEXT,
	PRIMARY KEY (competition_id, season_id)
);
CREATE TABLE events_5050 (
	event_id VARCHAR(50) PRIMARY KEY,
	outcome VARCHAR(40),
	outcome_id SMALLINT,
	counterpress BOOLEAN
);
CREATE TABLE events_badbehaviour (
	event_id VARCHAR(50) PRIMARY KEY,
	card VARCHAR(40),
	card_id SMALLINT
);
CREATE TABLE events_ballreceipt(
	event_id VARCHAR(50) PRIMARY KEY,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);
CREATE TABLE events_ballrecover(
	event_id VARCHAR(50) PRIMARY KEY,
	recovery_failure BOOLEAN,
	offensive BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_block (
	event_id VARCHAR(50) PRIMARY KEY,
	deflection BOOLEAN,
	offensive BOOLEAN,
	save_block BOOLEAN,
	counterpress BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_carry (
	event_id VARCHAR(50) PRIMARY KEY,
	end_loc_x numeric(5,2),
	end_loc_y numeric(5,2)
);
CREATE TABLE IF NOT EXISTS events_clearance (
	event_id VARCHAR(50) PRIMARY KEY,
	aerial_won BOOLEAN,
	head BOOLEAN,
	left_foot BOOLEAN,
	right_foot BOOLEAN,
	other BOOLEAN
);
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
	match_id VARCHAR(10),
	possession SMALLINT,
	possession_team VARCHAR(40),
	possession_team_id SMALLINT,
	play_pattern VARCHAR(40),
	play_pattern_id SMALLINT,
	position VARCHAR(40),
	position_id SMALLINT,
	loc_x numeric(5,2),
	loc_y numeric(5,2),
	duration NUMERIC(12,9),
	underpressure BOOLEAN
);
CREATE TABLE events_dribble (
	event_id VARCHAR(50) PRIMARY KEY,
	complete BOOLEAN,
    no_touch BOOLEAN,
    nutmeg BOOLEAN,
    overrun BOOLEAN
);
CREATE TABLE events_dribbledpass (
	event_id VARCHAR(50) PRIMARY KEY,
	counterpress BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_duel (
	event_id VARCHAR(50) PRIMARY KEY,
	type VARCHAR(20),
	type_id SMALLINT,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);
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
CREATE TABLE IF NOT EXISTS events_foulwon (
	event_id VARCHAR(50) PRIMARY KEY,
	defensive BOOLEAN,
	advantage BOOLEAN,
	penalty BOOLEAN
);
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
CREATE TABLE IF NOT EXISTS events_halfend (
	event_id VARCHAR(50) PRIMARY KEY,
	match_suspended BOOLEAN,
	early_video_end BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_halfstart (
	event_id VARCHAR(50) PRIMARY KEY,
	late_video_start BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_injurystoppage (
	event_id VARCHAR(50) PRIMARY KEY,
	in_chain BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_interception (
	event_id VARCHAR(50) PRIMARY KEY,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);
CREATE TABLE IF NOT EXISTS events_miscontrol (
	event_id VARCHAR(50) PRIMARY KEY,
	aerial_won BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_pass (
	event_id VARCHAR(50) PRIMARY KEY,
	-- team VARCHAR(40),
	-- team_id SMALLINT,
	-- player VARCHAR(60),
	-- player_id INT,
	recipient VARCHAR(60),
	recipient_id INT,
	type VARCHAR(16),
	type_id SMALLINT,
	technique VARCHAR(20),
	technique_id SMALLINT,
	end_loc_x numeric(5,2),
	end_loc_y numeric(5,2),
	outcome_id VARCHAR(3),
	outcome VARCHAR(40)
);
CREATE TABLE IF NOT EXISTS events_playeroff (
	event_id VARCHAR(50) PRIMARY KEY,
	permanent BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_pressure (
	event_id VARCHAR(50) PRIMARY KEY,
	counterpress BOOLEAN
);
CREATE TABLE IF NOT EXISTS events_shot (
	event_id VARCHAR(50) PRIMARY KEY,
	xg_score NUMERIC(10, 9),
	first_time BOOLEAN,
	end_location numeric[],
	technique_id INTEGER,
	technique_label VARCHAR(50),
	body_part_id INTEGER,
	body_part_label VARCHAR(50),
	type_id INTEGER,
	type_label VARCHAR(50),
	outcome_id INTEGER,
	outcome_label VARCHAR(50)
);
CREATE TABLE events_startingxi (
    event_id VARCHAR(50) PRIMARY KEY,
    match_id INTEGER,
    possession INTEGER,
    possession_team_id INTEGER,
    possession_team_name VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS events_substitution (
	event_id VARCHAR(50) PRIMARY KEY,
	replacement VARCHAR(60),
	replacement_id INT,
	outcome VARCHAR(40),
	outcome_id SMALLINT
);
CREATE TABLE IF NOT EXISTS lineups (
    match_id INTEGER,
    team_id INTEGER,
    team_name TEXT,
    player_id INTEGER,
    player_name TEXT,
	PRIMARY KEY (match_id, player_id)
);
CREATE TABLE IF NOT EXISTS matches (
    match_id VARCHAR(10) PRIMARY KEY,
    match_date DATE,
    kick_off TIME,
    competition_id INTEGER,
    competition VARCHAR(20),
    season VARCHAR(20),
    season_id INTEGER,
    home_team_id INTEGER,
    home_manager_id INTEGER,
    away_team_id INTEGER,
    away_manager_id INTEGER,
    home_score INTEGER,
    away_score INTEGER,
    match_status VARCHAR(20),
    match_status_360 VARCHAR(20),
    last_updated TIMESTAMP,
    last_updated_360 TIMESTAMP,
    match_week INTEGER,
    competition_stage_id INTEGER,
    stadium_id INTEGER,
    referee_id INTEGER
);
CREATE TABLE IF NOT EXISTS players (
	player_id INT PRIMARY KEY,
	player_name VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS tactics (
    event_id VARCHAR(50) PRIMARY KEY,
    formation INT,
    player_id INT[],
    player_name TEXT[],
    position_id INT[],
    position_name TEXT[],
    jersey_number INT[]
);

CREATE INDEX IF NOT EXISTS events_shot_index ON events_shot (event_id);
CREATE INDEX IF NOT EXISTS events_shot_index2 ON events_shot (technique_id);

CREATE INDEX IF NOT EXISTS events_pass_index ON events_pass (event_id);
CREATE INDEX IF NOT EXISTS events_pass_index2 ON events_pass (recipient_id);
CREATE INDEX IF NOT EXISTS events_pass_index3 ON events_pass (recipient);
CREATE INDEX IF NOT EXISTS events_pass_index4 ON events_pass (technique_id);

CREATE INDEX IF NOT EXISTS events_index ON events (match_id);
CREATE INDEX IF NOT EXISTS events_index2 ON events (player_id);
CREATE INDEX IF NOT EXISTS events_index3 ON events (player);
CREATE INDEX IF NOT EXISTS events_index4 ON events (team_id);
CREATE INDEX IF NOT EXISTS events_index5 ON events (team);

CREATE INDEX IF NOT EXISTS events_dribble_index1 ON events_dribble (event_id);

CREATE INDEX IF NOT EXISTS events_dribbledpass_index1 ON events_dribbledpass (event_id);

CREATE INDEX IF NOT EXISTS matches_index ON matches (season_id, competition_id);
CREATE INDEX IF NOT EXISTS matches_index2 ON matches (season_id);
CREATE INDEX IF NOT EXISTS matches_index3 ON matches (competition_id);
CREATE INDEX IF NOT EXISTS matches_index4 ON matches (match_id);

CREATE INDEX IF NOT EXISTS players_index ON players (player_id);
CREATE INDEX IF NOT EXISTS lineups_index ON lineups (match_id, player_id, team_id);

CREATE INDEX IF NOT EXISTS tactics_index ON tactics (event_id);