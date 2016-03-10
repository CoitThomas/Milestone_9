"""Verify if the function create_date_formats_table successfully creates an
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

def test_create_date_formats_table():
    """Assert the correct contents of the users table table."""
    # Create database.
    db_filename = 'test_create_date_formats_table.sqlite'
    date_formats_filename = 'test_date_formats.txt'

    database = sqlite3.connect(db_filename)
    cursor = database.cursor()

    data = create_database.get_data(date_formats_filename, 1)
    assert data, "Data for the 'date_formats' table test was not obtained."

    create_database.create_date_formats_table(cursor, data)

    # Check date_formats table.
    statement = """SELECT *
                       FROM date_formats
                       WHERE nationality =?"""
    assert query(statement, 'american', cursor) == (u'american',
                                                    u"'{month}/{day}/{year}'")
    assert query(statement, 'british', cursor) == (u'british',
                                                   u"'{day}/{month}/{year}'")
    assert query(statement, 'south korean', cursor) == (u'south korean',
                                                        u"'{year}/{month}/{day}'")

    database.close()
