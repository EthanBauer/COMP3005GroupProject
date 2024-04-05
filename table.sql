CREATE TABLE passes(
recipient references players,
length DECIMAL(2,6),
angle DECIMAL(3,8),
shot_assist BOOLEAN,
through_ball BOOLEAN
height REFERENCES heights,
end_location REFERENCES end_locations,
assisted_shot_id FOREIGN KEY,
shot_assist BOOLEAN,
body_part REFREENCES body_parts
);

CREATE TABLE events(
id SERIAL PRIMARY KEY,
index INT,
period INT,
timestamp TIME,
minute INT,
second INT,
type references types,
possession INT,
possession_team references possession_teams,
play_pattern references play_patterns,
team references teams,
player references players,
position references positions,
location decimal[],
duration DECIMAL(1,1),
related_events references events,
pass references passes);

CREATE TABLE lineup (
player_id SERIAL PRIMARY KEY,
team_id SERIAL FOREIGN KEY,
player_name varchar(255) NOT NULL,
player_nickname varchar(255),
jersey_name INT,
card references cards
position references positions);

CREATE TABLE lineups (
team_id SERIAL PRIMARY KEY,
team_name varchar(255) NOT NULL,
lineup REFERENCES lineup
);

CREATE TABLE competitions (
competition_id SERIAL PRIMARY KEY,
season_id SERIAL PRIMARY KEY,
country_name varchar(255) NOT NULL,
competition_name varchar(255) NOT NULL,
competition_gender varchar(6) NOT NULL,
competition_youth BOOLEAN,
competition_international BOOLEAN,
season_name varchar(255) NOT NULL,
match_updated DATE,
match_updated_360 DATE,
match_avaliable_360 DATE,
match_avaliable DATE);

CREATE TABLE home_teams(
name varchar(255),
nickname varchar(255),
home_team_gender varchar(6),
home_team_group varchar(255),
dob DATE,
country references countries,
managers references managers
);
CREATE TABLE away_teams(
name varchar(255),
nickname varchar(255),
away_team_gender varchar(6),
away_team_group varchar(255),
dob DATE,
country references countries,
managers references managers
);

CREATE TABLE matches(
match_id SERIAL PRIMARY KEY,
match_date DATE,
kick_off TIME,
competition references competitions,
season references seasons,
home_team references home_teams,
away_team references away_teams,
home_score INT,
away_score Int,
match_status varchar(255),
match_status_360 varchar(255),
last_updated DATETIME,
last_updated_360 DATETIME,
metadata refreences metadata,
match_week INT,
competiton_stage,
stadium refrences stadiums,
referee references referees
);