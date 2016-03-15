"""Take in a command line argument in the form:
python find_user.py <db_filename>.sqlite <username>
Print the username, nationality, and birthdate according to the
customary date format of the user's country and quit.
"""
import sqlite3
import sys
import username
import nationality
import birthdate
import database

def unpack_user_input(user_input):
    """Take in a list of user input containing a database filename and
    a user's username. Extract, validate, and return them as a tuple of
    string values.
    """
    assert len(user_input) < 3, "Too many arguments given."
    assert len(user_input) > 1, "Too few arguments given."

    db_filename = user_input[0]
    assert database.is_valid_name(db_filename), "Invalid database filename."

    user_username = user_input[1]
    assert username.is_valid(user_username), "Invalid username."

    return (db_filename, user_username)

def find_user(user_username, db_cursor):
    """Take in a string command line argument, 'user_input', and a
    database object, 'db_cursor'. If the username exists in the
    database, print the corresponding username, nationality and
    birthdate in the format appropriate to the user's nationality.
    Otherwise, print an error message.
    """
    assert username.is_valid(user_username), "Invalid username."
    select_statement = """SELECT username, users.nationality, birthdate, date_format
                       FROM users, date_formats
                       WHERE users.nationality = date_formats.nationality
                           AND username =?"""
    user = database.query(select_statement, user_username.lower(), db_cursor)

    if user:
        user_username = user[0]
        assert username.is_valid(user_username), "A valid username is missing."

        user_nationality = user[1]
        assert nationality.is_valid(user_nationality), "A valid nationality is missing."

        user_birthdate = user[2]
        assert birthdate.is_valid(user_birthdate), "A valid birthdate is missing."
        template = user[3]
        formatted_user_bday = birthdate.format_date(user_birthdate, template)
        return """username: %s
nationality: %s
birthdate: %s""" % (user_username, user_nationality, formatted_user_bday)
    else:
        return None

if __name__ == "__main__":
    # Get command line arguments.
    RAW_USER_INPUT = sys.argv[1:]
    USER_INPUT = [ITEM.lower() for ITEM in RAW_USER_INPUT]

    # Extract the database filename and the desired user's username.
    DB_FILENAME, USER_USERNAME = unpack_user_input(USER_INPUT)

    # Open and connect to a valid sqlite database.
    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()

    # Find and print the desired user from the database.
    USER = find_user(USER_USERNAME, CURSOR)
    if USER:
        print USER
    else:
        print None

    # Close database.
    DATABASE.close()
