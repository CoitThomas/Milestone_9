"""Read in a 'user data' text file and a 'format style' text file.
Write the files to an SQLite database file for storage.
"""
import sqlite3
import re
import ipdb

def read_file(file_name):
    """Read in data from a file and return it."""
    with open(file_name, 'r') as some_file:
        data = some_file.read()
    return data

def chunk_data(file_data, size):
    """Take in data as a string and an integer as a string. Return a
    list containing chunks of data that are 'size' number of lines
    each.
    """
    data_lines = file_data.splitlines()
    assert data_lines, "There is no data!"
    assert int(size), "An integer in the form of a string must be provided."
    assert 0 < int(size) <= len(data_lines), "A valid size must be provided."
    assert len(data_lines) % size == 0, "Data is incomplete."
    return [data_lines[pos:pos + size] for pos in range(0, len(data_lines), size)]

def parse(regex, group_name, data_chunk):
    """Take in a chunk of data. Parse the code according to a given
    regular expression. Group the parsed data according to a given
    group name and return it. If there is not a match, return None.
    """
    parsed_data = re.search(regex, data_chunk)
    return parsed_data.group(group_name) if parsed_data else None

def transpose_date(string):
    """Take in a string containing a date in the format mm/dd/yyyy and
    return a string conainting a date in the format yyyy-mm-dd.
    """
    month, day, year = parse_date(string)
    return '%s-%s-%s' % (year, month, day)

def parse_date(string):
    """Take in a string containing a date in the format mm/dd/yyyy and
    return three numerical strings representing a valid day, month, and
    year.
    """
    #ipdb.set_trace()
    date = re.search("(?P<month>[0-9]{1,2})" # Month.
                     "/(?P<day>[0-9]{1,2})" # Day.
                     "/(?P<year>[0-9]{4})", string) # Year.
    assert date, "A string in the format mm/dd/yyyy must be provided."

    month = make_int(date.group('month'))
    day = make_int(date.group('day'))
    year = make_int(date.group('year'))

    assert is_valid_date(month, day, year), "A valid date must be provided."

    return str(month), str(day), str(year)

def make_int(string):
    """Convert a given numerical string to an integer. If it cannot be
    converted, return None.
    """
    try:
        return int(string)
    except ValueError:
        return None

def is_valid_date(month, day, year):
    """Take in three integers representing a month, day, and year.
    Verify they are valid representations and return True or False.
    """
    return valid_month(month) and valid_day(day, month) and valid_year(year)

def valid_month(month):
    """Take in an integer representing a month of the year. Return True
    if it is valid. Otherwise, return False.
    """
    return 1 <= month <= 12

def valid_day(day, month):
    """Take in an integer representing a day and month of the year.
    Return True if it is a valid day for the given month. Otherwise,
    return False.
    """
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    assert valid_month(month)
    if month in month31:
        return 1 <= day <= 31
    if month in month30:
        return 1 <= day <= 30
    if month == 2:
        return 1 <= day <= 28

def valid_year(year):
    """Take in an integer representing a pertinent year. Return True if
    it is valid. Otherwise, return False.
    """
    return 1800 <= year <= 2200

def create_database(users_filename, date_formats_filename):
    """Create an SQLite database file."""
    database = sqlite3.connect(':memory:')
    cursor = database.cursor()

    # Create 'Users' table
    cursor.execute("""
        CREATE TABLE Users(Username text,
                           Nationality text,
                           Birthdate datetime)
    """)
    data = read_file(users_filename)
    assert data, "There is no data in file: %s" % users_filename
    data_chunks = chunk_data(data, 3)
    for chunk in data_chunks:
        username = parse(r"username:(?P<username>[\w.-]+)", 'username', chunk[0])
        nationality = parse("nationality:(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*)",
                            "nationality",
                            chunk[1],
                           )
        date = parse("birthdate:(?P<birthdate>[0-9]{1,2}/[0-9]{1,2}/[0-9]{4})",
                          "birthdate",
                          chunk[2],
                         )
        #ipdb.set_trace()
        birthdate = transpose_date(date)
        if username and nationality and birthdate:
            cursor.execute("""INSERT INTO Users(Username, Nationality, Birthdate)
                              VALUES(?,?,?)""", (username, nationality, birthdate))
    database.commit()

    # Create 'Date_Formats' table
    cursor.execute("""
        CREATE TABLE Date_Formats(Nationality text,
                                  Date_Format text,
    """)
    data = read_file(date_formats_filename)
    assert data, "There is no data in file: %s" % date_formats_filename
    data_chunks = chunk_data(data, 1)
    for chunk in data_chunks:
        nationality = parse("(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*),",
                            'nationality',
                            chunk)
        date_format = parse("(?P<date_format>'{month|day|year}/{month|day}/{day|year}')",
                            'date_format',
                            chunk)
    if nationality and date_format:
        cursor.execute("""INSERT INTO Date_Formats(Nationality, Date_Format)
                          VALUES (?,?)""", (nationality, date_format))
    database.commit()

    database.close()

if __name__ == "__main__":
    DB_FILENAME = 'myDatabase.db' # Insert desired database filename here.
    USER_FILENAME = 'user_data.txt' # Insert user filename here.
    FORMAT_FILENAME = 'date_formats.txt' # Insert format filename here.

    create_database(USER_FILENAME, FORMAT_FILENAME)

    DATABASE = sqlite3.connect(':memory:')
    CURSOR = DATABASE.cursor()
    CURSOR.execute("""SELECT Username, Nationality, Birthdate from Users""")
    USERS = CURSOR.fetchall()
    print 'Users:'
    print USERS
    CURSOR.execute("""SELECT Nationality, Date_Format from Date_Formats""")
    DATE_FORMATS = CURSOR.fetchall()
    print 'Date_Formats:'
    print DATE_FORMATS
