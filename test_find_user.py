"""Verify if the function find_user() correctly finds a given user in a
given database.
"""
import sqlite3
import create_database
from find_user import find_user
import read_file

def test_find_user():
    """Assert the correct return values of find_user() when given
    different username values to be found in the database.
    """
    # Create test database and tables.
    db_filename = 'test_find_user.sqlite'
    test_database = sqlite3.connect(db_filename)
    cursor = test_database.cursor()

    users_filename = 'test_user_data.txt'
    user_data_packages = read_file.get_data(users_filename, package_size=3)
    user_data_rows = [create_database.unpack_user_data(user_data_package)
                      for user_data_package in user_data_packages]
    create_database.create_users_table(cursor, user_data_rows)

    date_formats_filename = 'test_date_formats.txt'
    date_format_data_packages = read_file.get_data(date_formats_filename, package_size=1)
    date_format_data_rows = [create_database.unpack_date_format_data(date_format_data_package)
                             for date_format_data_package in date_format_data_packages]
    create_database.create_date_formats_table(cursor, date_format_data_rows)

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
    assert not find_user('margesimpson', cursor)

    test_database.close()
