"""Verify if the function create_users_table successfully creates an
SQLite table with the correct contents.
"""
import sqlite3
import create_database
import database
import read_file

def test_create_users_table():
    """Assert the correct contents of the users table table."""
    # Create database.
    db_filename = 'test_create_users_table.sqlite'
    test_database = sqlite3.connect(db_filename)
    cursor = test_database.cursor()

    users_filename = 'test_user_data.txt'
    user_data_packages = read_file.get_data(users_filename, package_size=3)
    user_data_rows = [create_database.unpack_user_data(user_data_package)
                      for user_data_package in user_data_packages]
    create_database.create_users_table(cursor, user_data_rows)

    # Check users table.
    statement = """SELECT *
                       FROM users
                       WHERE username =?"""
    assert database.query(statement, 'coit125', cursor) == (u'coit125',
                                                            u'american',
                                                            u'01/25/1984')
    assert database.query(statement, 'bcummberbatch', cursor) == (u'bcummberbatch',
                                                                  u'british',
                                                                  u'04/21/1978')
    assert database.query(statement, 'orangelover1107', cursor) == (u'orangelover1107',
                                                                    u'south korean',
                                                                    u'11/07/1983')

    test_database.close()
