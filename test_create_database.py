"""Verify if the function create_database() successfully creates an
SQLite database file with the correct content.
"""
import sqlite3
import create_database

def query(select_statement, search_term, db_filename):
    """Take in an SQL 'select_statement' as a string, a 'search_term' as
    a string, and a 'db_filename' as a string. Execute the query on the
    database and return the result.
    """
    database = sqlite3.connect(db_filename)
    cursor = database.cursor()
    cursor.execute(select_statement, (search_term,))
    row = cursor.fetchone()
    database.close()
    return row

def test_create_database():
    """Assert the correct contents of the users table and date_formats
    table.
    """
    db_filename = 'test_database.sqlite'
    user_filename = 'test_user_data.txt'
    format_filename = 'test_date_formats.txt'

    create_database.create_database(db_filename, user_filename, format_filename)

    # Check users table.
    statement = """SELECT *
                       FROM users
                       WHERE username =?"""
    assert query(statement, 'coit125', db_filename) == (u'coit125',
                                                        u'american',
                                                        u'01/25/1984')
    assert query(statement, 'bcummberbatch', db_filename) == (u'bcummberbatch',
                                                              u'british',
                                                              u'04/21/1978')
    assert query(statement, 'orangelover1107', db_filename) == (u'orangelover1107',
                                                                u'south korean',
                                                                u'11/07/1983')

    # Check date_formats table.
    statement = """SELECT *
                       FROM date_formats
                       WHERE nationality =?"""
    assert query(statement, 'american', db_filename) == (u'american',
                                                         u"'{month}/{day}/{year}'")
    assert query(statement, 'british', db_filename) == (u'british',
                                                        u"'{day}/{month}/{year}'")
    assert query(statement, 'south korean', db_filename) == (u'south korean',
                                                             u"'{year}/{month}/{day}'")
