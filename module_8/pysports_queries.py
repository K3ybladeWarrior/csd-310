import mysql.connector
from mysql.connector import errorcode 

config = {
    "user": "root",
    "password": "Lucipher69",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
db

cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

print("-- DISPLAYING TEAM RECORDS --")
for team in teams:

    print("Team ID: {} \nTeam Name: {} \nMascot: {} \n".format(team[0], team[1], team[2]))

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --") 

for player in players:

    print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))





