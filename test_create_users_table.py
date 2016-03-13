"""Verify if the function create_users_table successfully creates an
SQLite table with the correct contents.
"""
import sqlite3
import create_database
import database

def test_create_users_table():
    """Assert the correct contents of the users table table."""
    # Create database.
    db_file = 'test_create_users_table.sqlite'
    users_file = 'test_user_data.txt'

    test_database = sqlite3.connect(db_file)
    cursor = test_database.cursor()

    chunk_size = 3
    data = create_database.get_data_from_file(users_file, chunk_size)
    assert data, "Data for the 'users' table test was not obtained."
    create_database.create_users_table(cursor, data)

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
