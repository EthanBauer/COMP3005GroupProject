import os
import json
from pathlib import Path
import pandas as pd

directory = r'C:\Users\olymp\OneDrive\Documents\Git\open-data\data\lineups'
file_paths = Path(directory).glob("*.json")


player_data = {
    'file_number': [],
    'player_id': [],
    'player_name': [],
    'team_id': [],
    'team_name': [],
    'index': []}

for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        s = str(file_path)
        last_slash = s.rfind('/')
        dot_json = s.rfind('.json')
        file_number = s[last_slash + 1: dot_json]
        for entry in data:
            team_id = entry['team_id']
            team_name = entry['team_name']
            for player in entry['lineup']:
                player_id = player['player_id']
                player_name = player['player_name']
                index = file_number + str(player_id)
                player_data['file_number'].append(file_number)
                player_data['player_id'].append(player_id)
                player_data['player_name'].append(player_name)
                player_data['team_id'].append(team_id)
                player_data['team_name'].append(team_name)
                player_data['index'].append(index)
                print(f'index: {index}\nplayer_id: {player_id}\nplayer_name: {player_name}\nteam_id: {team_id}\nteam_name: {team_name}')

df = pd.DataFrame(player_data)