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

directory = r'C:\Users\mengx\Downloads\GithubRepo\open-data\data\events'
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
            
            event_data = {
                    'id': entry['id'],
                    'index': entry['index'],
                    'period': entry['period'],
                    'timestamp': entry['timestamp'],
                    'minute': entry['minute'],
                    'second': entry['second'],
                    'type_id': entry['type']['id'],
                    'type_name': entry['type']['name'],
                    'match_id': id
                }
            
            cursor.execute('''
                        INSERT INTO events (event_id, index, period, timestamp, minute,
                        second, type_id, type_name, match_id)
                        VALUES (%(id)s, %(index)s, %(period)s, %(timestamp)s,%(minute)s, %(second)s, %(type_id)s,%(type_name)s, %(match_id)s)
                    ''', event_data)
           
            # todo: add insert commands and table defn for the following events

            # 50-50
            if entry['type']['id'] == 33:
                secondary_event_data = {
                    'uid': entry['id'],
                    'outcome': entry['50_50']['outcome']['name'],
                    'outcome_id': entry['50_50']['outcome']['id'],
                    'counterpress': entry.get('counterpress', None)
                }

            # bad behaviour    
            elif entry['type']['id'] == 24:    
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    'card': entry['bad_behaviour']['card']['name'],
                    'card_id': entry['bad_behaviour']['card']['id']
                }
                # print(secondary_event_data)

            # ball receipt            
            elif entry['type']['id'] == 42:    
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'outcome': entry.get('ball_receipt')['outcome']['name'] if entry.get('ball_receipt') else None,
                    # 'outcome_id': entry.get('ball_receipt')['outcome']['id'] if entry.get('ball_receipt') else None,
                    'incomplete': True if entry.get('ball_receipt') else False
                }
                # print(secondary_event_data) 

            # ball recover    
            elif entry['type']['id'] == 2:   
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    'recovery_failure': True if entry.get('ball_recovery') and 'recovery_failure' in entry.get('ball_recovery') else False,
                    'offensive': True if entry.get('ball_recovery') and 'offensive' in entry.get('ball_recovery') else False,
                }

            # block
            elif entry['type']['id'] == 6:   
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    'deflection': True if entry.get('block') and 'deflection' in entry.get('block') else False,
                    'offensive': True if entry.get('block') and 'offensive' in entry.get('block') else False,
                    'save_block': True if entry.get('block') and 'save_block' in entry.get('block') else False,
                    'counterpass': True if entry.get('block') and 'counterpass' in entry.get('block') else False,
                }
                # print(secondary_event_data)
                
            # pass 
            elif entry['type']['id'] == 30:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    'team_id' : entry['team']['id'],
                    'team' : entry['team']['name'],
                    'player': entry['player']['name'],
                    'player_id': entry['player']['id'],
                    'recipient': entry['pass']['recipient']['name'] if entry['pass'].get('recipient') else None, # optional
                    'recipient_id': entry['pass']['recipient']['id'] if entry['pass'].get('recipient') else None,
                    'type': entry.get('pass')['type']['name'] if entry['pass'].get('type') else None, # optional
                    'type_id': entry.get('pass')['type']['id'] if entry['pass'].get('type') else None,
                    'technique': entry.get('pass')['technique']['name'] if entry['pass'].get('technique') else None,
                    'technique_id': entry.get('pass')['technique']['id'] if entry['pass'].get('technique') else None,
                    'end_loc_x': entry['pass']['end_location'][0],
                    'end_loc_y': entry['pass']['end_location'][1],
                    'outcome': entry['pass']['outcome']['name'] if entry['pass'].get('outcome') else None, # optional
                    'outcome_id': entry['pass']['outcome']['id'] if entry['pass'].get('outcome') else None,
                }

                cursor.execute('''
                        INSERT INTO events_pass (event_id, team, team_id, player, player_id, recipient, recipient_id, type, type_id, technique, technique_id, end_loc_x,
                        end_loc_y, outcome_id, outcome)
                        VALUES (%(uid)s, %(team)s, %(team_id)s, %(player)s, %(player_id)s, %(recipient)s, %(recipient_id)s, %(type)s, %(type_id)s, %(technique)s, %(technique_id)s, %(end_loc_x)s, %(end_loc_y)s, %(outcome_id)s, %(outcome)s)
                    ''', secondary_event_data)            
            
            # shot
            elif entry['type']['id'] == 16:
                # print(id)
                # print(entry['id'])

                secondary_event_data = {
                    'uid': entry['id'],
                    'team_id' : entry['team']['id'],
                    'team' : entry['team']['name'],
                    'player': entry['player']['name'],
                    'player_id': entry['player']['id'],
                    'xg_score': entry['shot']['statsbomb_xg']
                }

                cursor.execute('''
                        INSERT INTO events_shot (event_id, team, team_id, player, player_id, xg_score)
                        VALUES (%(uid)s, %(team)s, %(team_id)s, %(player)s, %(player_id)s, %(xg_score)s)
                    ''', secondary_event_data) 



print(filecount)

# todo: add code to parse events to 'events' database 