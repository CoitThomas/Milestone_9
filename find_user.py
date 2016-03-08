"""Take in one string command line argument in the form:
python find_user.py <username>
Print the username, nationality, and birthdate according to the user's
nationality and quit.
"""
import sys
import sqlite3
import date_validation

def find_user(username, db_filename):
    """Take in a string command line argument, 'username', and a
    string, 'db_filename'. If the username exists in the
    database, print the corresponding username, nationality and
    birthdate in the format appropriate to the user's nationality.
    Otherwise, print an error message.
    """
    database = sqlite3.connect(db_filename)
    cursor = database.cursor()
    sql_query = """SELECT birthdate, date_format
                       FROM users, date_formats
                       WHERE users.nationality = date_formats.nationality
                           AND username =?"""
    cursor.execute(sql_query, (username,))
    user = cursor.fetchone()
    if user:
        p_month, p_day, p_year = date_validation.parse_date(user[0])
        print user[1].format(month=p_month, day=p_day, year=p_year)
    else:
        print "Error, user not found."
    database.close()

if __name__ == "__main__":
    DB_FILENAME = 'myDatabase.sqlite' # Insert desired database filename here.
    find_user(str(sys.argv[1:]), DB_FILENAME)
