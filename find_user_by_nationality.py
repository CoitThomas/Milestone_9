"""Take in a command line argument in the form:
python find_user_by_nationality.py <db_filename>.sqlite <nationality>
Print the usernames of all the users in the database of the specified
nationality and quit.
"""
import sqlite3
import get

def find_user_by_nationality(user_input, db_cursor):
    """Take in a string command line argument, 'nationality', and a
    string, 'db_filename'. If the nationality exists in the database,
    print the usernames of all the users in the database of that
    nationality. Otherwise, print an error message.
    """
    sql_query = """SELECT username
                       FROM users
                       WHERE nationality =?"""
    db_cursor.execute(sql_query, (user_input.lower(),))
    users = db_cursor.fetchall()

    if users:
        return [user[0] for user in users]
    else:
        return ["Error, no users of that nationality were found."]

if __name__ == "__main__":
    USER_INPUT = get.get_cmd_ln_arguments(3, 2)

    DB_FILENAME = get.get_db_filename(USER_INPUT, 0)

    if len(USER_INPUT) == 3:
        USER_INPUT = [USER_INPUT[1]+' '+USER_INPUT[2]]
        NATIONALITY = get.get_nationality(USER_INPUT, 0)
    else:
        NATIONALITY = get.get_nationality(USER_INPUT, 1)

    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()

    USERS = find_user_by_nationality(NATIONALITY, CURSOR)
    for USER in USERS:
        print USER

    DATABASE.close()
