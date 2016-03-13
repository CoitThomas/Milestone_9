"""Verify if the function create_date_formats_table successfully creates an
SQLite table with the correct contents.
"""
import sqlite3
import create_database
import database

def test_create_date_formats_table():
    """Assert the correct contents of the users table table."""
    # Create database.
    db_file = 'test_create_date_formats_table.sqlite'
    date_formats_file = 'test_date_formats.txt'

    test_database = sqlite3.connect(db_file)
    cursor = test_database.cursor()

    chunk_size = 1
    data = create_database.get_data_from_file(date_formats_file, chunk_size)
    assert data, "Data for the 'date_formats' table test was not obtained."
    create_database.create_date_formats_table(cursor, data)

    # Check date_formats table.
    statement = """SELECT *
                       FROM date_formats
                       WHERE nationality =?"""
    assert database.query(statement, 'american', cursor) == (u"american",
                                                             u"{month}/{day}/{year}")
    assert database.query(statement, 'british', cursor) == (u"british",
                                                            u"{day}/{month}/{year}")
    assert database.query(statement, 'south korean', cursor) == (u"south korean",
                                                                 u"{year}/{month}/{day}")

    test_database.close()
