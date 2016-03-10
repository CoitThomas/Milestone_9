"""Verify if the function create_users_table successfully creates an
SQLite table with the correct contents.
"""
import sqlite3
import create_database

def query(select_statement, search_term, db_cursor):
    """Take in an SQL 'select_statement' as a string, a 'search_term' as
    a string, and a 'db_filename' as a string. Execute the query on the
    database and return the result.
    """
    db_cursor.execute(select_statement, (search_term,))
    row = db_cursor.fetchone()
    return row

def test_create_users_table():
    """Assert the correct contents of the users table table."""
    # Create database.
    db_filename = 'test_create_users_table.sqlite'
    users_filename = 'test_user_data.txt'

    database = sqlite3.connect(db_filename)
    cursor = database.cursor()

    data = create_database.get_data(users_filename, 3)
    assert data, "Data for the 'users' table test was not obtained."

    create_database.create_users_table(cursor, data)

    # Check users table.
    statement = """SELECT *
                       FROM users
                       WHERE username =?"""
    assert query(statement, 'coit125', cursor) == (u'coit125',
                                                   u'american',
                                                   u'01/25/1984')
    assert query(statement, 'bcummberbatch', cursor) == (u'bcummberbatch',
                                                         u'british',
                                                         u'04/21/1978')
    assert query(statement, 'orangelover1107', cursor) == (u'orangelover1107',
                                                           u'south korean',
                                                           u'11/07/1983')

    database.close()
