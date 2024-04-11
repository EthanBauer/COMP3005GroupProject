import psycopg
# psycopg 
# pip install psycopg
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
    
# get useful match ids from the match table  
conn = connect_db()
cursor = conn.cursor()
# cursor.execute("SELECT match_id FROM public.matches ORDER BY match_id ASC; ")
# id_list = [row[0] for row in cursor.fetchall()]
# conn.close()

id_list = [15946, 15956, 15973, 15978, 15986, 15998, 16010, 16023, 16029, 16056, 16073, 16079, 16086, 16095, 16109, 16120, 16131, 16136, 16149, 16157, 16173, 16182, 16190, 16196, 16205, 16215, 16231, 16240, 16248, 16265, 16275, 16289, 16306, 16317, 303377, 303400, 303421, 303430, 303451, 303470, 303473, 303479, 303487, 303493, 303504, 303516, 303517, 303524, 303532, 303548, 303596, 303600, 303610, 303615, 303634, 303652, 303664, 303666, 303674, 303680, 303682, 303696, 303700, 303707, 303715, 303725, 303731, 3749052, 3749068, 3749079, 3749108, 3749117, 3749133, 3749153, 3749192, 3749196, 3749233, 3749246, 3749253, 3749257, 3749274, 3749276, 3749278, 3749296, 3749310, 3749346, 3749358, 3749360, 3749403, 3749431, 3749434, 3749448, 3749453, 3749454, 3749462, 3749465, 3749493, 3749522, 3749526, 3749528, 3749552, 3749590, 3749603, 3749631, 3749642, 3764440, 3764661, 3773369, 3773372, 3773377, 3773386, 3773387, 3773403, 3773415, 3773428, 3773457, 3773466, 3773474, 3773477, 3773497, 3773523, 3773526, 3773547, 3773552, 3773565, 3773571, 3773585, 3773586, 3773587, 3773593, 3773597, 3773625, 3773631, 3773656, 3773660, 3773661, 3773665, 3773672, 3773689, 3773695]

# print(id_list)
# print(len(id_list))

# directory = r'C:\Users\mengx\Downloads\GithubRepo\open-data\data\events'
directory = r'/Users/ethanbauer/Downloads/W2024/COMP3005/GithubRepo/open-data-master/data/events'
# file_pathes = Path(directory).glob("*.json")

filecount = 0 
for id in id_list:
    fp = os.path.join(directory, str(id)+".json")
    print(fp)
    with open(fp, 'r', encoding='utf-8') as f:
        filecount += 1 
        data = json.load(f)
        print(id)
        for entry in data:
            # insert common event data to 'events' table
            # todo: add more common attributes to event table
            print(id)
            print(entry['id'])

            # shot
            if entry['type']['id'] == 16:
                # print(id)
                # print(entry['id'])

                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'xg_score': entry['shot']['statsbomb_xg'],
                    'first_time': entry['shot']['first_time'] if entry['shot'].get('first_time') else False,
                    'end_location': entry['shot']['end_location'] if entry['shot'].get('end_location') else None
                }

                cursor.execute('''
                        INSERT INTO events_shot (event_id, xg_score, first_time, end_location)
                        VALUES (%(uid)s, %(xg_score)s, %(first_time)s, %(end_location)s)
                    ''', secondary_event_data) 