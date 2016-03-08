"""Take in one string command line argument in the form:
python find_user.py <username>
Print the username, nationality, and birthdate according to the user's
nationality and quit.
"""
import sys
import sqlite3
import re
import date_validation
from parse import parse

def find_user(string, db_filename):
    """Take in a string command line argument, 'username', and a
    string, 'db_filename'. If the username exists in the
    database, print the corresponding username, nationality and
    birthdate in the format appropriate to the user's nationality.
    Otherwise, print an error message.
    """
    database = sqlite3.connect(db_filename)
    cursor = database.cursor()

    line = re.sub("[',]", "", string.lower())
    regex = r"(?P<username>[\w.-]+)"
    username = parse(regex, 'username', line)

    sql_query = """SELECT username, users.nationality, birthdate, date_format
                       FROM users, date_formats
                       WHERE users.nationality = date_formats.nationality
                           AND username =?"""
    cursor.execute(sql_query, (username,))
    user = cursor.fetchone()
    database.close()
    if user:
        p_month, p_day, p_year = date_validation.parse_date(user[2])
        username = user[0]
        nationality = user[1]
        birthdate = user[3].format(month=p_month, day=p_day, year=p_year).strip("'")
        return """username: %s
nationality: %s
birthdate: %s""" % (username, nationality, birthdate)
    else:
        return "Error, user not found."

if __name__ == "__main__":
    DB_FILENAME = 'database.sqlite' # Insert desired database filename here.
    print find_user(str(sys.argv[1:]), DB_FILENAME)
