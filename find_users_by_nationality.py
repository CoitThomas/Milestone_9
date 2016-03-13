"""Take in a command line argument in the form:
python find_users_by_nationality.py <db_filename>.sqlite <nationality>
Print the usernames of all the users in the database of the specified
nationality and quit.
"""
import sqlite3
import sys
import nationality
import database

def unpack_user_input(user_input):
    """Take in a list of user input containing a database filename and
    a nationality. Extract, validate, and return them as a tuple of
    string values.
    """
    assert len(user_input) < 4, "Too many arguments given."
    assert len(user_input) > 1, "Too few arguments given."

    db_filename = user_input[0]
    assert database.is_valid_name(db_filename), "Invalid database filename."

    if len(user_input) == 3:
        desired_nationality = nationality.get(user_input[1]+' '+user_input[2])
    else:
        desired_nationality = nationality.get(user_input[1])
    assert desired_nationality, "Invalid nationality."

    return (db_filename, desired_nationality)

def find_users_by_nationality(desired_nationality, db_cursor):
    """Take in a string command line argument, 'nationality', and a
    string, 'db_filename'. If the nationality exists in the database,
    print the usernames of all the users in the database of that
    nationality. Otherwise, print an error message.
    """
    select_statement = """SELECT username
                       FROM users
                       WHERE nationality =?"""
    users = database.query_all(select_statement, desired_nationality.lower(), db_cursor)
    return [user[0] for user in users] if users else ["No users of that nationality were found."]

if __name__ == "__main__":
    # Get command line arguments.
    RAW_USER_INPUT = sys.argv[1:]
    USER_INPUT = [ITEM.lower() for ITEM in RAW_USER_INPUT]

    # Extract the database filename and the desired nationality.
    DB_FILENAME, DESIRED_NATIONALITY = unpack_user_input(USER_INPUT)

    # Open and connect to a valid sqlite database.
    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()

    # Find and print all the users of the specified nationality from the database.
    USERS = find_users_by_nationality(DESIRED_NATIONALITY, CURSOR)
    for USER in USERS:
        print USER

    # Close database.
    DATABASE.close()
