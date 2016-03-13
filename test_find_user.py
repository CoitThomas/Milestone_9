"""Verify if the function find_user() correctly finds a given user in a
given database.
"""
import sqlite3
import create_database
from find_user import find_user

def test_find_user():
    """Assert the correct return values of find_user() when given
    different username values to be found in the database.
    """
    # Create test database and tables.
    db_filename = 'test_find_user.sqlite'
    users_filename = 'test_user_data.txt'
    date_formats_filename = 'test_date_formats.txt'

    test_database = sqlite3.connect(db_filename)
    cursor = test_database.cursor()

    chunk_size = 3
    data = create_database.get_data_from_file(users_filename, chunk_size)
    assert data, "Data for the 'users' table was not obtained."
    create_database.create_users_table(cursor, data)

    chunk_size = 1
    data = create_database.get_data_from_file(date_formats_filename, chunk_size)
    assert data, "Data for the 'date_formats' table was not obtained."
    create_database.create_date_formats_table(cursor, data)

    template = """username: %s
nationality: %s
birthdate: %s"""

    # Check mm/dd/yyyy style user.
    assert find_user('coit125', cursor) == template % ('coit125',
                                                       'american',
                                                       '1/25/1984')
    # Check dd/mm/yyyy style user.
    assert find_user('bcummberbatch', cursor) == template % ('bcummberbatch',
                                                             'british',
                                                             '21/4/1978')
    # Check yyyy/mm/dd style user.
    assert find_user('orangelover1107', cursor) == template % ('orangelover1107',
                                                               'south korean',
                                                               '1983/11/7')
    # Check case-sensitivity.
    assert find_user('COIT125', cursor) == template % ('coit125',
                                                       'american',
                                                       '1/25/1984')
    # Check non-user.
    assert find_user('margesimpson', cursor) == "User not found."

    test_database.close()
