"""Take in a command line argument in the form:
python find_user.py <db_filename>.sqlite <username>
Print the username, nationality, and birthdate according to the
customary date format of the user's country and quit.
"""
import sqlite3
import get

def find_user(user_input, db_cursor):
    """Take in a string command line argument, 'user_input', and a
    database object, 'db_cursor'. If the username exists in the
    database, print the corresponding username, nationality and
    birthdate in the format appropriate to the user's nationality.
    Otherwise, print an error message.
    """
    sql_query = """SELECT username, users.nationality, birthdate, date_format
                       FROM users, date_formats
                       WHERE users.nationality = date_formats.nationality
                           AND username =?"""
    db_cursor.execute(sql_query, (user_input.lower(),))
    user = db_cursor.fetchone()

    if user:
        username = get.get_username(user, 0)
        nationality = get.get_nationality(user, 1)
        birthdate = get.get_birthdate(user, 2, 3)
        return """username: %s
nationality: %s
birthdate: %s""" % (username, nationality, birthdate)
    else:
        return "Error, user not found."

if __name__ == "__main__":
    USER_INPUT = get.get_cmd_ln_arguments(2, 2)

    DB_FILENAME = get.get_db_filename(USER_INPUT, 0)
    USERNAME = get.get_username(USER_INPUT, 1)

    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()

    print find_user(USERNAME, CURSOR)

    DATABASE.close()
