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
            print(id)
            print(entry['id'])
            if entry['type']['id'] != 35:
                event_data = {
                        'id': entry['id'],
                        'team_id' : entry['team']['id'],
                        'team' : entry['team']['name'],
                        'player': entry['player']['name'] if entry.get('player') else None,
                        'player_id': entry['player']['id'] if entry.get('player') else None,
                        'index': entry['index'],
                        'period': entry['period'],
                        'timestamp': entry['timestamp'],
                        'minute': entry['minute'],
                        'second': entry['second'],
                        'type_id': entry['type']['id'],
                        'type_name': entry['type']['name'],
                        'match_id': id
                    }
            
                # cursor.execute('''
                #             INSERT INTO events (event_id, team, team_id, player, player_id, index, period, timestamp, minute,
                #             second, type_id, type_name, match_id)
                #             VALUES (%(id)s, %(team)s, %(team_id)s, %(player)s,%(player_id)s, %(index)s, %(period)s, %(timestamp)s,%(minute)s, %(second)s, %(type_id)s,%(type_name)s, %(match_id)s)
                #         ''', event_data)
           

            # 50-50
            if entry['type']['id'] == 33:
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'outcome': entry['50_50']['outcome']['name'],
                    'outcome_id': entry['50_50']['outcome']['id'],
                    'counterpress': entry.get('counterpress', None)
                }
                # cursor.execute('''
                #         INSERT INTO events_5050 (event_id,
                #         outcome, outcome_id, counterpress)
                #         VALUES (%(uid)s, %(outcome)s, %(outcome_id)s,%(counterpress)s)
                #     ''', secondary_event_data)

            # bad behaviour    
            elif entry['type']['id'] == 24:    
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'card': entry['bad_behaviour']['card']['name'],
                    'card_id': entry['bad_behaviour']['card']['id']
                }
                # cursor.execute('''
                #         INSERT INTO events_badbehaviour (event_id, card, card_id)
                #         VALUES (%(uid)s, %(card)s, %(card_id)s)
                #     ''', secondary_event_data)

            # ball receipt            
            elif entry['type']['id'] == 42:    
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    # 'incomplete': True if entry.get('ball_receipt') else False
                    'outcome': entry.get('ball_receipt')['outcome']['name'] if entry.get('ball_receipt') else None,
                    'outcome_id': entry.get('ball_receipt')['outcome']['id'] if entry.get('ball_receipt') else None,
                }
                # cursor.execute('''
                #         INSERT INTO events_ballreceipt (event_id, outcome, outcome_id)
                #         VALUES (%(uid)s, %(outcome)s, %(outcome_id)s)
                #     ''', secondary_event_data)
                
            # ball recover    
            elif entry['type']['id'] == 2:   
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    'recovery_failure': True if entry.get('ball_recovery') and 'recovery_failure' in entry.get('ball_recovery') else False,
                    'offensive': True if entry.get('ball_recovery') and 'offensive' in entry.get('ball_recovery') else False,
                }
                # cursor.execute('''
                #         INSERT INTO events_ballrecover (event_id, recovery_failure, offensive)
                #         VALUES (%(uid)s, %(recovery_failure)s, %(offensive)s)
                #     ''', secondary_event_data) 

            # block
            elif entry['type']['id'] == 6:   
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    'deflection': True if entry.get('block') and 'deflection' in entry.get('block') else False,
                    'offensive': True if entry.get('block') and 'offensive' in entry.get('block') else False,
                    'save_block': True if entry.get('block') and 'save_block' in entry.get('block') else False,
                    'counterpress': True if entry.get('block') and 'counterpress' in entry.get('block') else False,
                }
                # cursor.execute('''
                #         INSERT INTO events_block (event_id, deflection, offensive, save_block, counterpress)
                #         VALUES (%(uid)s, %(deflection)s, %(offensive)s, %(save_block)s, %(counterpress)s)
                #     ''', secondary_event_data) 
                
            # carry 
            elif entry['type']['id'] == 43:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'end_loc_x': entry['carry']['end_location'][0],
                    'end_loc_y': entry['carry']['end_location'][1]
                }
                # cursor.execute('''
                #         INSERT INTO events_carry (event_id, end_loc_x, end_loc_y)
                #         VALUES (%(uid)s, %(end_loc_x)s, %(end_loc_y)s)
                #     ''', secondary_event_data) 

            # clearance
            elif entry['type']['id'] == 9:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'aerial_won': True if entry['clearance'].get('aerial_won') else False,
                    'head' : True if entry['clearance'].get('head') else False, 
                    'left_foot' : True if entry['clearance'].get('left_foot') else False, 
                    'right_foot' : True if entry['clearance'].get('right_foot') else False, 
                    'other' : True if entry['clearance'].get('other') else False, 
                }
                # cursor.execute('''
                #         INSERT INTO events_clearance (event_id, aerial_won, head, left_foot, right_foot)
                #         VALUES (%(uid)s, %(aerial_won)s, %(head)s, %(left_foot)s, %(right_foot)s)
                #     ''', secondary_event_data) 
            # Duel 
            elif entry['type']['id'] == 4:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'type': entry['duel']['type']['name'],
                    'type_id': entry['duel']['type']['id'],
                    'outcome': entry['duel']['outcome']['name'] if entry.get('duel').get('outcome') else None,
                    'outcome_id': entry['duel']['outcome']['id'] if entry.get('duel').get('outcome') else None
                }
                # cursor.execute('''
                #         INSERT INTO events_duel (event_id, type, type_id, outcome, outcome_id)
                #         VALUES (%(uid)s, %(type)s, %(type_id)s, %(outcome)s, %(outcome_id)s)
                #     ''', secondary_event_data) 

            # Foul Committed  22
            elif entry['type']['id'] == 22:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'counterpress': True if entry.get('foul_committed') and 'counterpress' in entry.get('foul_committed') else False,
                    'offensive': True if entry.get('foul_committed') and 'offensive' in entry.get('foul_committed') else False,
                    'advantage': True if entry.get('foul_committed') and 'advantage' in entry.get('foul_committed') else False,
                    'penalty': True if entry.get('foul_committed') and 'penalty' in entry.get('foul_committed') else False,
                    'type': entry['foul_committed']['type']['name'] if entry.get('foul_committed') and entry.get('foul_committed').get('type') else None,
                    'type_id': entry['foul_committed']['type']['id'] if entry.get('foul_committed') and entry.get('foul_committed').get('type') else None,
                    'card': entry['foul_committed']['card']['name'] if entry.get('foul_committed') and entry.get('foul_committed').get('card') else None,
                    'card_id': entry['foul_committed']['card']['id'] if entry.get('foul_committed') and entry.get('foul_committed').get('card') else None,
                }
                # cursor.execute('''
                #         INSERT INTO events_foulcommitted (event_id, counterpress, offensive, advantage, penalty, type, type_id, card, card_id)
                #         VALUES (%(uid)s, %(counterpress)s, %(offensive)s, %(advantage)s,  %(penalty)s, %(type)s,  %(type_id)s, %(card)s, %(card_id)s)
                #     ''', secondary_event_data) 
            
            # Foul Won  21
            elif entry['type']['id'] == 21:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'defensive': True if entry.get('foul_won') and 'defensive' in entry.get('foul_won') else False,
                    'advantage': True if entry.get('foul_won') and 'advantage' in entry.get('foul_won') else False,
                    'penalty': True if entry.get('foul_won') and 'penalty' in entry.get('foul_won') else False
                }

                # cursor.execute('''
                #         INSERT INTO events_foulwon (event_id, defensive, advantage, penalty)
                #         VALUES (%(uid)s, %(defensive)s,  %(advantage)s, %(penalty)s)
                #     ''', secondary_event_data) 
            
            # Goalkeeper  23
            elif entry['type']['id'] == 23:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],

                    'position': entry['goalkeeper']['position']['name'] if entry['goalkeeper'].get('position') else None,
                    'position_id': entry['goalkeeper']['position']['id'] if entry['goalkeeper'].get('position') else None,

                    'technique': entry['goalkeeper']['technique']['name'] if entry['goalkeeper'].get('technique') else None,
                    'technique_id': entry['goalkeeper']['technique']['id'] if entry['goalkeeper'].get('technique') else None,

                    'body_part': entry['goalkeeper']['body_part']['name'] if entry['goalkeeper'].get('body_part') else None,
                    'body_part_id': entry['goalkeeper']['body_part']['id'] if entry['goalkeeper'].get('body_part') else None,

                    'type': entry['goalkeeper']['type']['name'] if entry['goalkeeper'].get('type') else None,
                    'type_id': entry['goalkeeper']['type']['id'] if entry['goalkeeper'].get('type') else None,

                    'outcome': entry['goalkeeper']['outcome']['name'] if entry['goalkeeper'].get('outcome') else None,
                    'outcome_id': entry['goalkeeper']['outcome']['id'] if entry['goalkeeper'].get('outcome') else None,
                }

                # cursor.execute('''
                #         INSERT INTO events_goalkeeper (event_id, position, position_id, technique, technique_id, body_part, body_part_id, type, type_id, outcome, outcome_id)
                #         VALUES (%(uid)s, %(position)s, %(position_id)s, %(technique)s, %(technique_id)s, %(body_part)s, %(body_part_id)s, %(type)s, %(type_id)s, %(outcome)s, %(outcome_id)s)
                #     ''', secondary_event_data) 

            # Half End  34
            elif entry['type']['id'] == 34:
                secondary_event_data = {
                    'uid': entry['id'],
                    # indeed the following two are all false 
                    'match_suspended': True if entry.get('half_end') and 'match_suspended' in entry.get('half_end') else False,
                    'early_video_end': True if entry.get('half_end') and 'early_video_end' in entry.get('half_end') else False,
                    # 'match_suspended2': True if entry.get('match_suspended') else False,
                    # 'early_video_end2': True if entry.get('early_video_end') else False,
                }
                # cursor.execute('''
                #         INSERT INTO events_halfend (event_id, match_suspended, early_video_end)
                #         VALUES (%(uid)s, %(match_suspended)s,  %(early_video_end)s)
                #     ''', secondary_event_data) 

            # Half Start  18
            elif entry['type']['id'] == 18:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    'late_video_start': True if entry.get('half_start') and 'late_video_start' in entry.get('half_start') else False
                }

                # cursor.execute('''
                #         INSERT INTO events_halfstart (event_id, late_video_start)
                #         VALUES (%(uid)s, %(late_video_start)s)
                #     ''', secondary_event_data) 

            # Injury Stoppage 40
            elif entry['type']['id'] == 40:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'in_chain': True if entry.get('injury_stoppage') and 'in_chain' in entry.get('injury_stoppage') else False,
                }
                # cursor.execute('''
                #         INSERT INTO events_injurystoppage (event_id, in_chain)
                #         VALUES (%(uid)s, %(in_chain)s)
                #     ''', secondary_event_data) 

            # Interception  10
            elif entry['type']['id'] == 10:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'outcome': entry['interception']['outcome']['name'] if entry['interception'].get('outcome') else None, # optional
                    'outcome_id': entry['interception']['outcome']['id'] if entry['interception'].get('outcome') else None,
                }
                # cursor.execute('''
                #         INSERT INTO events_interception (event_id, outcome, outcome_id)
                #         VALUES (%(uid)s, %(outcome)s, %(outcome_id)s)
                #     ''', secondary_event_data) 

            # Miscontrol  38
            elif entry['type']['id'] == 38:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'aerial_won': True if entry.get('miscontrol') and 'aerial_won' in entry.get('miscontrol') else False,
                }
                # cursor.execute('''
                #         INSERT INTO events_miscontrol (event_id, aerial_won)
                #         VALUES (%(uid)s, %(aerial_won)s)
                #     ''', secondary_event_data) 

# =========
            # player off  27 permanent all false
            elif entry['type']['id'] == 27:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    # 'permanent2': True if entry.get('permanent') else False,
                    'permanent': True if entry.get('player_off') and 'permanent' in entry.get('player_off') else False,
                }
                
                # cursor.execute('''
                #         INSERT INTO events_playeroff (event_id, permanent)
                #         VALUES (%(uid)s, %(permanent)s)
                #     ''', secondary_event_data) 

            # todo nothing special should add more attributes to the main event
            # player on  26
            # shield 28

            # pressure 17  
            elif entry['type']['id'] == 17:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'counterpress': True if entry.get('counterpress') else False
                }
                # cursor.execute('''
                #         INSERT INTO events_pressure (event_id, counterpress)
                #         VALUES (%(uid)s, %(counterpress)s)
                #     ''', secondary_event_data) 
                
            # substitution 19
            elif entry['type']['id'] == 19:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'replacement': entry['substitution']['replacement']['name'] if entry['substitution'].get('replacement') else None,
                    'replacement_id': entry['substitution']['replacement']['id'] if entry['substitution'].get('replacement') else None,
                    'outcome': entry['substitution']['outcome']['name'] if entry['substitution'].get('outcome') else None,
                    'outcome_id': entry['substitution']['outcome']['id'] if entry['substitution'].get('outcome') else None,
                }
                # cursor.execute('''
                #         INSERT INTO events_substitution (event_id, replacement, replacement_id, outcome, outcome_id)
                #         VALUES (%(uid)s, %(replacement)s, %(replacement_id)s, %(outcome)s, %(outcome_id)s)
                #     ''', secondary_event_data) 

            # pass 
            elif entry['type']['id'] == 30:
                # print(id)
                # print(entry['id'])
                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
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

                # cursor.execute('''
                #         INSERT INTO events_pass (event_id, recipient, recipient_id, type, type_id, technique, technique_id, end_loc_x,
                #         end_loc_y, outcome_id, outcome)
                #         VALUES (%(uid)s, %(recipient)s, %(recipient_id)s, %(type)s, %(type_id)s, %(technique)s, %(technique_id)s, %(end_loc_x)s, %(end_loc_y)s, %(outcome_id)s, %(outcome)s)
                #     ''', secondary_event_data)            
            
            # shot
            elif entry['type']['id'] == 16:
                # print(id)
                # print(entry['id'])

                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'xg_score': entry['shot']['statsbomb_xg'],
                    'first_time': entry['shot']['first_time'] if entry['shot'].get('first_time') else False
                }

                # cursor.execute('''
                #         INSERT INTO events_shot (event_id, xg_score, first_time)
                #         VALUES (%(uid)s, %(xg_score)s, %(first_time)s)
                #     ''', secondary_event_data) 

            # dribble
            elif entry['type']['id'] == 14:
                # print(id)
                # print(entry['id'])

                secondary_event_data = {
                    'uid': entry['id'],
                    # 'team_id' : entry['team']['id'],
                    # 'team' : entry['team']['name'],
                    # 'player': entry['player']['name'],
                    # 'player_id': entry['player']['id'],
                    'complete': True if entry['dribble']['outcome']['name']== 'Complete' else False,
                    'overrun': True if entry['dribble'].get('overrun') else False,
                    'nutmeg': True if entry['dribble'].get('nutmeg') else False,
                    'no_touch': True if entry['dribble'].get('no_touch') else False
                }

                # cursor.execute('''
                #         INSERT INTO events_dribble (event_id, complete, no_touch, nutmeg, overrun)
                #         VALUES (%(uid)s, %(complete)s, %(no_touch)s, %(nutmeg)s, %(overrun)s)
                #     ''', secondary_event_data) 
        

            # dribbled_pass
            elif entry['type']['id'] == 39:
                # print(id)
                # print(entry['id'])

                secondary_event_data = {
                    'uid': entry['id'],
                    'team_id' : entry['team']['id'],
                    'team' : entry['team']['name'],
                    'player': entry['player']['name'],
                    'player_id': entry['player']['id'],
                    # seems like events interested have counterpress false
                    'counterpress': True if entry.get('dribbled_pass') and 'counterpress' in entry.get('dribbled_pass') else False,
                }

                # if (secondary_event_data['counterpress']):
                #     print(secondary_event_data)

                # cursor.execute('''
                #         INSERT INTO events_dribbledpass (event_id, counterpress)
                #         VALUES (%(uid)s, %(counterpress)s)
                #     ''', secondary_event_data) 

print(filecount)

# todo: add code to parse events to 'events' database 