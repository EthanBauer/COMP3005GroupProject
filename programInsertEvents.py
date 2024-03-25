import psycopg2
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
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        connection.autocommit = True
        return connection
    # catch error and print out 
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None
    
conn = connect_db()
cursor = conn.cursor()
cursor.execute("SELECT match_id FROM public.matches ORDER BY match_id ASC; ")
id_list = [row[0] for row in cursor.fetchall()]
conn.close()
# get useful match ids from the match table

print(id_list)
print(len(id_list))

directory = r'C:\Users\mengx\Downloads\GithubRepo\open-data\data\events'
# file_pathes = Path(directory).glob("*.json")

filecount = 0 
for id in id_list:
    fp = os.path.join(directory, str(id)+".json")
    print(fp)
    with open(fp, 'r', encoding='utf-8') as f:
        filecount += 1 

print(filecount)

# todo: add code to parse events to 'events' database 