import psycopg
import json
from pathlib import Path

# Usage: 

# modify connection parameters
dbname = 'projecttest'
user = 'postgres'
password = 'postgres'
host = '127.0.0.1'  
port = '5432'  

# modify matches data directory 
directory = r'C:\Users\mengx\Downloads\GithubRepo\open-data\data\matches'

# copy and execute matches.sql in pgadmin
# python programInsertMatches.py

# other constants but probably no need to modify
# seasons interested
seasons = ["2003/2004", "2020/2021", "2019/2020", "2018/2019"] 

# competitions interested
comps = [2,11]
# 2 Premier League  11 La Liga

# Helper function to connect to postgres server
def connect_db():
    try:
        # connect to server with psycopg2
        connection = psycopg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        connection.autocommit = True
        return connection
    # catch error and print out 
    except psycopg.Error as e:
        print("Error connecting to the database:", e)
        return None
    

file_pathes = Path(directory).glob("**/*.json")
conn = connect_db()
cursor = conn.cursor()

for fp in file_pathes:
    # print(fp)
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for entry in data:
            if entry['competition']['competition_id'] in comps and entry['season']['season_name'] in seasons: 
                # print(entry['match_id'])
                match_data = {
                    'match_id': entry['match_id'],
                    'match_date': entry['match_date'],
                    'kick_off': entry['kick_off'],
                    'competition_id': entry['competition']['competition_id'],
                    'season': entry['season']['season_name'],
                    'season_id': entry['season']['season_id'],
                    'home_team_id': entry['home_team']['home_team_id'],
                    'home_manager_id': entry['home_team'].get('managers')[0]['id'] if entry['home_team'].get('managers') else None, # there are entries without managers all matches interest have at most 1 manager
                    'away_team_id': entry['away_team']['away_team_id'], 
                    'away_manager_id': entry['away_team'].get('managers')[0]['id'] if entry['away_team'].get('managers') else None, # there are entries without managers
                    'home_score': entry['home_score'],
                    'away_score': entry['away_score'],
                    'match_status': entry['match_status'],
                    'match_status_360': entry['match_status_360'],
                    'last_updated': entry['last_updated'],
                    'last_updated_360': entry['last_updated_360'],
                    'match_week': entry['match_week'],
                    'competition_stage_id': entry['competition_stage']['id'],
                    'stadium_id': entry.get('stadium', {}).get('id'), # there are entries without stadium info
                    'referee_id': entry.get('referee', {}).get('id') #entry['referee']['id'] not work bc there are entries without referee
                }

                cursor.execute('''
                        INSERT INTO matches (match_id, match_date, kick_off, competition_id, season, season_id,
                        home_team_id, home_manager_id, away_team_id, away_manager_id,
                        home_score, away_score, match_status, match_status_360,
                        last_updated, last_updated_360, match_week, competition_stage_id,
                        stadium_id, referee_id)
                        VALUES (%(match_id)s, %(match_date)s, %(kick_off)s, %(competition_id)s, %(season)s, %(season_id)s,
                        %(home_team_id)s, %(home_manager_id)s, %(away_team_id)s, %(away_manager_id)s,
                        %(home_score)s, %(away_score)s, %(match_status)s, %(match_status_360)s,
                        %(last_updated)s, %(last_updated_360)s, %(match_week)s, %(competition_stage_id)s,
                        %(stadium_id)s, %(referee_id)s)
                    ''', match_data)
        # exit()
                
conn.close()
            


