import mysql.connector

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

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

records = cursor.fetchall() 

print("-- DISPLAYING PLAYER RECORDS --")

for record in records:

    print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {} \n".format(record[0], record[1], record[2] , record[3]))