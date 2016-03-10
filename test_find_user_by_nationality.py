"""Verify if the function find_user_by_nationality() correctly returns
every user of a given nationality.
"""
import sqlite3
import create_database
from find_user_by_nationality import find_user_by_nationality

def test_find_user():
    """Assert the correct list of users returned from the database when
    the function find_user_by_nationality is given various
    nationalities as input.
    """
    # Create test database and tables.
    db_filename = 'test_find_user_by_nationality.sqlite'
    users_filename = 'test_user_data.txt'

    database = sqlite3.connect(db_filename)
    cursor = database.cursor()

    data = create_database.get_data(users_filename, 3)
    assert data, "Data for the 'users' table was not obtained."
    create_database.create_users_table(cursor, data)

    error_msg = 'Error, no users of that nationality were found.'

    # Check database for a nationality with 1 user.
    assert find_user_by_nationality('south korean', cursor) == ['orangelover1107']

    # Check database for a nationality with multiple users.
    assert find_user_by_nationality('american', cursor) == ['coit125', 'austinwiltshire']

    # Check database for a nationality with 0 users.
    assert find_user_by_nationality('gondorian', cursor) == [error_msg]

    # Check case-sensitivity.
    assert find_user_by_nationality('BRITISH', cursor) == ['bcummberbatch']
