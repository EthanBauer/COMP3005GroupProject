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