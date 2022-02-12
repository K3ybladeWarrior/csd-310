#connecting to database
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

#set variable to use cursor()
cursor = db.cursor()

#allows me to execute SQL commands
cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")

#save to database
db.commit()

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

#variable to hold data from line 24
records = cursor.fetchall() 


print("-- DISPLAYING PLAYERS AFTER INSERT --")

for record in records:

    print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {} \n".format(record[0], record[1], record[2] , record[3]))

cursor.execute("UPDATE player SET team_id =2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'") 

db.commit()

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

records = cursor.fetchall() 

print("-- DISPLAYING PLAYERS AFTER UPDATE --")

for record in records:

    print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {} \n".format(record[0], record[1], record[2] , record[3]))

cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")

db.commit()

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

records = cursor.fetchall() 

print("-- DISPLAYING PLAYERS AFTER DELETE --")

for record in records:

    print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {} \n".format(record[0], record[1], record[2] , record[3]))