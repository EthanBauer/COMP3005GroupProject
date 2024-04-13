import psycopg
import os
import json
from pathlib import Path

# Define connection parameters
dbname = 'projecttest'
user = 'postgres'
password = 'postgres'
host = '127.0.0.1'  
port = '5432'  

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
    
conn = connect_db()
cursor = conn.cursor()


directory = r'/Users/ethanbauer/Downloads/W2024/COMP3005/GithubRepo/open-data-master/data/lineups'
file_paths = Path(directory).glob("*.json")

for filepath in file_paths:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        s = str(filepath)
        last_slash = s.rfind('/')
        dot_json = s.rfind('.json')
        file_number = s[last_slash + 1: dot_json]
        for entry in data:
            match_id = file_number
            team_id = entry['team_id']
            team_name = entry['team_name']
            for player in entry['lineup']:
                player_id = player['player_id']
                player_name = player['player_name']
                lineup_data = {
                    'match_id': match_id,
                    'team_id': team_id,
                    'team_name': team_name,
                    'player_id': player_id,
                    'player_name': player_name
                }
                cursor.execute('''
                        INSERT INTO lineups (match_id, team_id, team_name, player_id, player_name)
                        VALUES (%(match_id)s, %(team_id)s, %(team_name)s, %(player_id)s, %(player_name)s)
                    ''', lineup_data)