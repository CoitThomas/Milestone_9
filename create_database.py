"""Read in a 'user data' text file and a 'format style' text file.
Write the files to an SQLite database file for storage.
"""
import sqlite3
import date_validation
from parse import parse

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

def create_database(db_filename, users_filename, date_formats_filename):
    """Create an SQLite database file."""
    database = sqlite3.connect(db_filename)
    cursor = database.cursor()

    # Create 'users' table
    cursor.execute("""
        CREATE TABLE users(username TEXT PRIMARY KEY,
                           nationality TEXT,
                           birthdate DATE)
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
        birthdate = parse("birthdate:(?P<birthdate>[0-9]{1,2}/[0-9]{1,2}/[0-9]{4})",
                          "birthdate",
                          chunk[2],
                         )
        if username and nationality and birthdate:
            assert date_validation.is_valid_str_date(birthdate), "A valid date must be provided."
            cursor.execute("""INSERT INTO users(username, nationality, birthdate)
                              VALUES(?,?,?)""", (username, nationality, birthdate))
    database.commit()

    # Create 'date_formats' table
    cursor.execute("""
        CREATE TABLE date_formats(nationality TEXT PRIMARY KEY,
                                  date_format TEXT)
    """)
    data = read_file(date_formats_filename)
    assert data, "There is no data in file: %s" % date_formats_filename
    data_chunks = chunk_data(data, 1)
    for chunk in data_chunks:
        if chunk:
            nationality = parse("(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*),",
                                'nationality',
                                chunk[0])
            date_format = parse("(?P<date_format>'{[a-zA-Z]+}/{[a-zA-Z]+}/{[a-zA-Z]+}')",
                                'date_format',
                                chunk[0])
            if nationality and date_format:
                cursor.execute("""INSERT INTO date_formats(nationality, date_format)
                                  VALUES (?,?)""", (nationality, date_format))
    database.commit()

    database.close()

if __name__ == "__main__":
    DB_FILENAME = 'myDatabase.sqlite' # Insert desired database filename here.
    USER_FILENAME = 'user_data.txt' # Insert user filename here.
    FORMAT_FILENAME = 'date_formats.txt' # Insert format filename here.

    create_database(DB_FILENAME, USER_FILENAME, FORMAT_FILENAME)

    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()
    CURSOR.execute("""SELECT * FROM users""")
    USERS = CURSOR.fetchall()
    print 'Users:'
    print USERS
    CURSOR.execute("""SELECT * FROM date_formats""")
    DATE_FORMATS = CURSOR.fetchall()
    print 'Date_Formats:'
    print DATE_FORMATS

    DATABASE.close()
