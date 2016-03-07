"""Take in one string command line argument in the form:
python find_user.py <username>
Print the username, nationality, and birthdate according to the user's
nationality and quit.
"""
import sys
import re
import sqlite3
import create_database

def parse_date(string):
    """Take in a string containing a date in the format mm/dd/yyyy and
    return three numerical strings representing a valid day, month, and
    year.
    """
    date = re.search("(?P<month>[0-9]{1,2})" # Month.
                     "/(?P<day>[0-9]{1,2})" # Day.
                     "/(?P<year>[0-9]{4})", string) # Year.
    assert date, "A string in the format mm/dd/yyyy must be provided."

    month = create_database.make_int(date.group('month'))
    day = create_database.make_int(date.group('day'))
    year = create_database.make_int(date.group('year'))

    assert create_database.is_valid_date(month, day, year), "A valid date must be provided."

    return str(month), str(day), str(year)

def find_user(argv, db_filename):
    database = sqlite3.connect(db_filename)
    cursor = database.cursor()
    sql_query = """SELECT birthdate, date_format
                       FROM users, date_formats
                       WHERE users.nationality = date_formats.nationality
                           AND username =?"""
    cursor.execute(sql_query, (argv,))
    user = cursor.fetchone()
    if user:
        mm, dd, yyyy = parse_date(user[0])
        print user[1].format(month=mm, day=dd, year=yyyy)
    else:
        print "Sorry, username not found."
	database.close()

if __name__ == "__main__":
   DB_FILENAME = 'myDatabase.sqlite' # Insert desired database filename here.
   find_user(str(sys.argv[1]), DB_FILENAME)
