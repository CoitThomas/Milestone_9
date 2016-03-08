"""Take in one string command line argument in the form:
python find_user_by_nationality.py <nationality>
Print the usernames of all the users in the database of the specified
nationality and quit.
"""
import sys
import sqlite3
import re
from parse import parse

def find_user_by_nationality(string, db_filename):
    """Take in a string command line argument, 'nationality', and a
    string, 'db_filename'. If the nationality exists in the database,
    print the usernames of all the users in the database of that
    nationality. Otherwise, print an error message.
    """
    database = sqlite3.connect(db_filename)
    cursor = database.cursor()

    line = re.sub("[',]", "", string.lower())
    regex = "(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*)"
    nationality = parse(regex, 'nationality', line)

    sql_query = """SELECT username
                       FROM users
                       WHERE nationality =?"""
    cursor.execute(sql_query, (nationality,))
    users = cursor.fetchall()
    database.close()
    if users:
        user_list = []
        for user in users:
            user_list.append(user[0])
        return user_list
    else:
        return ["Error, no users of that nationality were found."]

if __name__ == "__main__":
    DB_FILENAME = 'database.sqlite' # Insert desired database filename here.
    USERS = find_user_by_nationality(str(sys.argv[1:]), DB_FILENAME)
    for USER in USERS:
        print USER
