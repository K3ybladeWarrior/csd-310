#Lucy Garcia
#Data / Database security
#whatabook_program.py
#final project



#database config

import mysql.connector

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
db

cursor = db.cursor()


#drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS store")
cursor.execute("DROP TABLE IF EXISTS wishlist")
cursor.execute("DROP TABLE IF EXISTS book")
cursor.execute("DROP TABLE IF EXISTS user")



#save to database
db.commit()

#Creating tables; store
cursor.execute("CREATE TABLE store (store_id INT NOT NULL AUTO_INCREMENT, locale VARCHAR(500) NOT NULL, PRIMARY KEY(store_id))")

#book
cursor.execute("CREATE TABLE book (book_id INT NOT NULL AUTO_INCREMENT, book_name VARCHAR(200) NOT NULL, details VARCHAR(500), author VARCHAR(200) NOT NULL, PRIMARY KEY(book_id))")

#user
cursor.execute("CREATE TABLE user (user_id INT NOT NULL AUTO_INCREMENT, first_name VARCHAR(75) NOT NULL, last_name VARCHAR (75) NOT NULL, PRIMARY KEY(user_id))")

#wishlist
cursor.execute("CREATE TABLE wishlist (wishlist_id INT NOT NULL AUTO_INCREMENT, user_id INT NOT NULL, book_id INT NOT NULL, PRIMARY KEY(wishlist_id), FOREIGN KEY(user_id) REFERENCES user(user_id), FOREIGN KEY(book_id) REFERENCES book(book_id))")

db.commit()

#Insert data into store table
cursor.execute("INSERT INTO store(store_id,locale) VALUES (1, '1400 Windy Street Oxnard, Ca 92700')")

#Insert data into book table
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (1,'IT', 'Horror story about a killer clown', 'Stephen King')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (2, 'Odd Thomas', 'Story about an odd fellow', 'Stephen King')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (3, 'Clifford', 'A big red dog', 'Norman Bridwell')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (4, 'Christine', 'A killer car has a deep obsession with the owner', 'Stephen King')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (5, 'Cujo', 'A dog has a killer case of rabies', 'Stephen King')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (6, 'Pet Sematary', 'A father buries his kids dead cat in an indian burial ground', 'Stephen King')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (7, 'The Mist', 'A thick mist engulfs a sleepy town. Then, giant monsters begin to attack!', 'Stephen King')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (8, 'Misery', 'an author is rescued by an obsessive fan but the attraction is FATAL', 'Stephen King')")
cursor.execute("INSERT INTO book(book_id, book_name, details, author) VALUES (9, 'The Girl Who Loved Tom Gordon', 'A little girl gets lost at a pit stop on her way to a ball game', 'Stephen King')")

#Insert data into user table
cursor.execute("INSERT INTO user(user_id,first_name,last_name) VALUES (1, 'Lucy', 'Garcia')")

cursor.execute("INSERT INTO user(user_id,first_name,last_name) VALUES (2, 'Marley', 'Perez')")

cursor.execute("INSERT INTO user(user_id,first_name,last_name) VALUES (3, 'Nancy', 'Perez')")

#Insert data into wishlist table
cursor.execute("INSERT INTO wishlist(wishlist_id,user_id,book_id) VALUES (1,1,6)")
cursor.execute("INSERT INTO wishlist(wishlist_id,user_id,book_id) VALUES (2,2,4)")
cursor.execute("INSERT INTO wishlist(wishlist_id,user_id,book_id) VALUES (3,3,5)")

db.commit()

