import psycopg
import json
import os

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
    
# insert "2003/2004", "2020/2021", "2019/2020", "2018/2019" la liga info from competitions.json

directory = r'C:\Users\mengx\Downloads\GithubRepo\open-data\data'
with open(os.path.join(directory, 'competitions.json')) as f:
    data = json.load(f)

conn = connect_db()
cursor = conn.cursor()

seasons = ["2003/2004", "2020/2021", "2019/2020", "2018/2019"]
competiton_name = ["La Liga", "Premier League"]
for entry in data:
    if entry.get("competition_name") in competiton_name  and entry.get("season_name") in seasons:
        cursor.execute('''INSERT INTO competitions (competition_id, season_id, country_name, competition_name,
                                                        competition_gender, competition_youth, competition_international,
                                                        season_name)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                       (entry["competition_id"], entry["season_id"], entry["country_name"],
                        entry["competition_name"], entry["competition_gender"], entry["competition_youth"],
                        entry["competition_international"], entry["season_name"]))
conn.close()
