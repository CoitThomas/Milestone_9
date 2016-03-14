"""Read in a 'user data' text file and a 'format style' text file.
Write the files to an SQLite database file for storage.
"""
import sqlite3
import username
import nationality
import birthdate
import date_format
import read_file

def unpack_user_data(user_data_package):
    """Take in a list, 'user_data_package', which contains a user's
    username, nationality, and birthdate. If all three elements are in
    the package, return a tuple of the elements. Otherwise, return
    None.
    """
    assert len(user_data_package) == 3, "Wrong amount of information in data package."
    user_username = username.get_from_label(user_data_package[0].lower())
    user_nationality = nationality.get_from_label(user_data_package[1].lower())
    user_birthdate = birthdate.get_from_label(user_data_package[2])

    if user_username and user_nationality and user_birthdate:
        return (user_username, user_nationality, user_birthdate)
    else:
        return None

def unpack_date_format_data(date_format_data_package):
    """Take in a list, 'date_format_data_package', which contains a
    date_format and the nationality associated with that format. If
    both elements are in the package, return a tuple of the elements.
    Otherwise, return None.
    """
    assert len(date_format_data_package) == 1, "Wrong amount of information in the data package."
    user_nationality = nationality.get(date_format_data_package[0].lower())
    national_date_format = date_format.get(date_format_data_package[0].lower())

    if user_nationality and national_date_format:
        return (user_nationality, national_date_format)
    else:
        return None

def create_users_table(db_cursor, data_rows):
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
    for data_row in data_rows:
        if data_row:
            assert len(data_row) == 3, "Wrong amount of information in the data row."
            db_cursor.execute("""INSERT INTO users(username, nationality, birthdate)
                              VALUES(?,?,?)""", (data_row))

def create_date_formats_table(db_cursor, data_rows):
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
    for data_row in data_rows:
        if data_row:
            assert len(data_row) == 2, "Wrong amount of information in the data row."
            db_cursor.execute("""INSERT INTO date_formats(nationality, date_format)
                              VALUES (?,?)""", (data_row))

if __name__ == "__main__":
    # Create a new database and connect to it.
    DB_FILENAME = 'database.sqlite' # Insert desired database filename here.
    DATABASE = sqlite3.connect(DB_FILENAME)
    DB_CURSOR = DATABASE.cursor()

    # Create 'users' table in database.
    USERS_FILENAME = 'user_data.txt' # Insert user filename here.
    USER_DATA_PACKAGES = read_file.get_data(USERS_FILENAME, package_size=3)
    USER_DATA_ROWS = [unpack_user_data(USER_DATA_PACKAGE)
                      for USER_DATA_PACKAGE in USER_DATA_PACKAGES]
    create_users_table(DB_CURSOR, USER_DATA_ROWS)

    # Create 'date_formats' table in database.
    DATE_FORMATS_FILENAME = 'date_formats.txt' # Insert format filename here.
    DATE_FORMAT_DATA_PACKAGES = read_file.get_data(DATE_FORMATS_FILENAME, package_size=1)
    DATE_FORMAT_DATA_ROWS = [unpack_date_format_data(DATE_FORMAT_DATA_PACKAGE)
                             for DATE_FORMAT_DATA_PACKAGE in DATE_FORMAT_DATA_PACKAGES]
    create_date_formats_table(DB_CURSOR, DATE_FORMAT_DATA_ROWS)

    # Save and close the database.
    DATABASE.commit()
    DATABASE.close()

    print "Database finished. Filename: %s" % DB_FILENAME
