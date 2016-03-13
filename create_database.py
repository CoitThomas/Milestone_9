"""Read in a 'user data' text file and a 'format style' text file.
Write the files to an SQLite database file for storage.
"""
import sqlite3
import username
import nationality
import birthdate
import date_format

def unpack_user_data(user_data):
    """Extract the username, nationality, and birthdate of the user
    from the data object 'user_data' and return them.
    """
    assert len(user_data) == 3
    user_username = username.get(user_data[0].lower())
    user_nationality = nationality.get(user_data[1].lower())
    user_birthdate = birthdate.get(user_data[2])

    return (user_username, user_nationality, user_birthdate)

def unpack_date_format_data(date_format_data):
    """Extract a nationality and date_format from the data object
    'date_format_data' and return them.
    """
    assert len(date_format_data) == 1
    user_nationality = nationality.get(date_format_data[0].lower())
    national_date_format = date_format.get(date_format_data[0].lower())

    return (user_nationality, national_date_format)

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

def get_data_from_file(filename, chunk_size):
    """Take in a string 'filename' and an integer 'chunk_size'. Read in
    the data from the file and divide the data into chunks that are
    'chunk_size' number of lines each. Return a list containing the
    chunks of data.
    """
    data = read_file(filename)
    assert data, "There is no data in file: %s" % filename
    return chunk_data(data, chunk_size)

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
        assert len(chunk) == 3, "Wrong amount of information in data chunk."
        user_username, user_nationality, user_birthdate = unpack_user_data(chunk)
        if user_username and user_nationality and user_birthdate:
            db_cursor.execute("""INSERT INTO users(username, nationality, birthdate)
                              VALUES(?,?,?)""", (user_username.lower(),
                                                 user_nationality.lower(),
                                                 user_birthdate))

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
        assert len(chunk) == 1, "Wrong amoun of information in data chunk."
        user_nationality, national_date_format = unpack_date_format_data(chunk)
        if user_nationality and national_date_format:
            db_cursor.execute("""INSERT INTO date_formats(nationality, date_format)
                              VALUES (?,?)""", (user_nationality.lower(),
                                                national_date_format.lower()))

if __name__ == "__main__":
    DB_FILE = 'database.sqlite' # Insert desired database filename here.
    USERS_FILE = 'user_data.txt' # Insert user filename here.
    DATE_FORMATS_FILE = 'date_formats.txt' # Insert format filename here.

    # Create a new database and connect to it.
    DATABASE = sqlite3.connect(DB_FILE)
    CURSOR = DATABASE.cursor()

    # Create 'users' table in database.
    CHUNK_SIZE = 3 # Number of lines of text from the .txt file desired in each chunk of data.
    USER_DATA = get_data_from_file(USERS_FILE, CHUNK_SIZE)
    create_users_table(CURSOR, USER_DATA)

    # Create 'date_formats' table in database.
    CHUNK_SIZE = 1 # Number of lines of text from the .txt file desired in each chunk of data.
    DATE_FORMAT_DATA = get_data_from_file(DATE_FORMATS_FILE, CHUNK_SIZE)
    create_date_formats_table(CURSOR, DATE_FORMAT_DATA)

    # Save and close the database.
    DATABASE.commit()
    DATABASE.close()

    print "Database finished. Filename: %s" % DB_FILE
