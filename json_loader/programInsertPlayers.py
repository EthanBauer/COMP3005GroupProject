#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:17:01 2024

@author: ethanbauer
"""

import psycopg
import os
import json
from pathlib import Path

# modify connection parameters
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

directory = r'/Users/ethanbauer/Downloads/W2024/COMP3005/GithubRepo/open-data-master/data/lineups'
file_paths = Path(directory).glob("*.json")

for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for entry in data:
            for player in entry['lineup']:
                player_data = {
                    'player_id': player['player_id'],
                    'player_name': player['player_name']
                }          
                cursor.execute('''
                        INSERT INTO players (player_id, player_name)
                        VALUES (%(player_id)s, %(player_name)s)
                        ON CONFLICT (player_id) DO NOTHING
                    ''', player_data)