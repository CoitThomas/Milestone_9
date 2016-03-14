"""Verify if the function find_users_by_nationality() correctly returns
every user of a given nationality.
"""
import sqlite3
import create_database
from find_users_by_nationality import find_users_by_nationality
import read_file

def test_find_users_by_nationality():
    """Assert the correct list of users returned from the database when
    the function find_user_by_nationality is given various
    nationalities as input.
    """
    # Create test database and tables.
    db_filename = 'test_find_user_by_nationality.sqlite'
    database = sqlite3.connect(db_filename)
    cursor = database.cursor()

    users_filename = 'test_user_data.txt'
    user_data_packages = read_file.get_data(users_filename, package_size=3)
    user_data_rows = [create_database.unpack_user_data(user_data_package)
                      for user_data_package in user_data_packages]
    create_database.create_users_table(cursor, user_data_rows)

    # Check database for a nationality with 1 user.
    assert find_users_by_nationality('south korean', cursor) == ['orangelover1107']

    # Check database for a nationality with multiple users.
    assert find_users_by_nationality('american', cursor) == ['coit125', 'austinwiltshire']

    # Check database for a nationality with 0 users.
    assert not find_users_by_nationality('gondorian', cursor)

    # Check case-sensitivity.
    assert find_users_by_nationality('BRITISH', cursor) == ['bcummberbatch']
