import os
import json
from pathlib import Path
import pandas as pd

directory = r'/Users/ethanbauer/Downloads/W2024/COMP3005/GithubRepo/open-data-master/data/lineups'
file_paths = Path(directory).glob("*.json")


lineup_data = {
    'match_id': [],
    'team_id': [],
    'team_name': [],
    'player_id': [],
    'player_name': []
    }

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
                lineup_data['match_id'].append(match_id)
                lineup_data['team_id'].append(team_id)
                lineup_data['team_name'].append(team_name)
                lineup_data['player_id'].append(player_id)
                lineup_data['player_name'].append(player_name)
df = pd.DataFrame(lineup_data)