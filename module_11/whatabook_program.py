#Lucy Garcia
#Data / Database security
#whatabook_program.py
#final project

import sys
import mysql.connector
from mysql.connector import errorcode

#database config
#needed to connect to db
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#methods

#display menu options
def show_menu():
    print("\nWelcome to Whatabook!")

    print("\n 1. View Books\n 2. View Store Locations\n 3. View My Account\n 4. Exit Program")

    try:
        choice = int(input('\nEnter menu choice: '))

        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)


#display books
def show_books(_cursor):
    _cursor.execute("SELECT * FROM book")

    # get the results from the cursor
    books = _cursor.fetchall()

    print("\nBook List\n")
    
    #for loop to grab all books in table
    for book in books:
        print("  Book ID: {}\n  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[3], book[2]))

def show_locations(_cursor):
    _cursor.execute("SELECT * FROM store")

    locations = _cursor.fetchall()

    print("\nSTORE LOCATIONS")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))


def validate_user():   
    user_id = int(input("Please enter your User ID: "))

    if user_id not in range(1,5,1):
        print("Sorry, that User ID does not exist. Exiting program.")
        sys.exit(0)

    
    return user_id
    sys.exit(0)

def show_account_menu():
    try:
        print("\nCustomer Menu")
        print("1. Wishlist\n2. Add Book\n3. Main Menu")
        account_option = int(input('Enter menu choice: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    if not wishlist:
        print("You don't currently have a wishlist. Please add a book to start one.")
    else:
        print("\nWISHLIST ITEMS")
        for book in wishlist:
            print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    query = ("SELECT * FROM book " +
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\nAVAILABLE BOOKS")

    for book in books_to_add:
        print("Book Id: {}\nBook Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # connect to the WhatABook database 
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()

    user_selection = show_menu()

#loop with if statement depending on user_selection value
    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            #nested while loop to capture if statements when account_option not 3
            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)

                    #ask user their book selection
                    book_id = int(input("\nEnter the id of the book you want to add to your wishlist: "))
                    
                    #add  selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    #captures changes to db
                    db.commit()

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show the account menu 
                account_option = show_account_menu()
        
        if user_selection < 0 or user_selection > 4:
            print("\nThat option does not exist. Please try again.")
            
        user_selection = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    #close db connection
    db.close()