"""Read in a 'user data' text file and a 'format style' text file.
Write the files to an SQLite database file for storage.
"""
import sqlite3
import re
import date_validation

def read_file(file_name):
    """Read in data from a file and return it."""
    with open(file_name, 'r') as some_file:
        data = some_file.read()
    return data

def chunk_data(file_data, size):
    """Take in data as a string and an integer 'size'. Return a
    list containing chunks of data that are 'size' number of lines
    each.
    """
    data_lines = file_data.splitlines()
    assert data_lines, "There is no data!"
    assert isinstance(size, int), "An integer must be provided."
    assert 0 < size <= len(data_lines), "A valid size must be provided."
    assert len(data_lines) % size == 0, "Data is incomplete."
    return [data_lines[pos:pos + size] for pos in range(0, len(data_lines), size)]

def get_data(filename, chunk_size):
    """Take in a string 'filename' and an integer 'chunk_size'. Read in
    the data from the file and divide the data into chunks that are
    'chunk_size' number of lines each. Return a list containing the
    chunks of data.
    """
    data = read_file(filename)
    assert data, "There is no data in file: %s" % filename
    return chunk_data(data, chunk_size)

def parse(regex, group_name, string):
    """Take in a string. Parse the string according to a given
    regular expression. Group the parsed data according to a given
    group name and return it. If there is not a match, return None.
    """
    parsed_data = re.search(regex, string)
    return parsed_data.group(group_name) if parsed_data else None

def create_users_table(db_cursor, data_chunks):
    """Create a table of users with columns for username, nationality,
    and birthdate and insert the data found in the given users file.
    """
    # Create users table in the given database.
    db_cursor.execute("""
        CREATE TABLE users(username TEXT PRIMARY KEY,
                           nationality TEXT,
                           birthdate DATE)
    """)
    # Insert data into the users table.
    for chunk in data_chunks:
        username = parse(r"username:(?P<username>[\w.-]+)",
                         'username',
                         chunk[0],
                        )
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
            db_cursor.execute("""INSERT INTO users(username, nationality, birthdate)
                              VALUES(?,?,?)""", (username.lower(), nationality.lower(), birthdate))

def create_date_formats_table(db_cursor, data_chunks):
    """Create a table of date formats with columns for nationality and
    the date format and insert the data found in the given date_formats
    file.
    """
    # Create date_formats table in the given database.
    db_cursor.execute("""
        CREATE TABLE date_formats(nationality TEXT PRIMARY KEY,
                                  date_format TEXT)
    """)
    # Insert data into the date_formats table.
    for chunk in data_chunks:
        nationality = parse("(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*),",
                            'nationality',
                            chunk[0],
                           )
        date_format = parse("(?P<date_format>'{[a-zA-Z]+}/{[a-zA-Z]+}/{[a-zA-Z]+}')",
                            'date_format',
                            chunk[0],
                           )
        if nationality and date_format:
            db_cursor.execute("""INSERT INTO date_formats(nationality, date_format)
                              VALUES (?,?)""", (nationality.lower(), date_format))

if __name__ == "__main__":
    DB_FILENAME = 'database.sqlite' # Insert desired database filename here.
    USERS_FILENAME = 'user_data.txt' # Insert user filename here.
    DATE_FORMATS_FILENAME = 'date_formats.txt' # Insert format filename here.

    # Create a new database and connect to it.
    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()

    # Create 'users' table in database.
    DATA = get_data(USERS_FILENAME, 3)
    assert DATA, "Data for the 'users' table was not obtained."
    create_users_table(CURSOR, DATA)

    # Create 'date_formats' table in database.
    DATA = get_data(DATE_FORMATS_FILENAME, 1)
    assert DATA, "Data for the 'date_formats' table was not obtained."
    create_date_formats_table(CURSOR, DATA)

    # Save and close the database.
    DATABASE.commit()
    DATABASE.close()

    print "Database finished. Filename: %s" % DB_FILENAME
