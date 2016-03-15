"""Verify if the function create_date_formats_table successfully creates an
SQLite table with the correct contents.
"""
import sqlite3
import create_database
import database
import read_file

def test_create_date_formats_table():
    """Assert the correct contents of the users table table."""
    # Create database.
    db_filename = 'test_create_date_formats_table.sqlite'
    test_database = sqlite3.connect(db_filename)
    cursor = test_database.cursor()

    date_formats_filename = 'test_date_formats.txt'
    date_format_data_packages = read_file.get_data(date_formats_filename, package_size=1)
    date_format_data_rows = [create_database.unpack_date_format_data(date_format_data_package)
                             for date_format_data_package in date_format_data_packages]
    create_database.create_date_formats_table(cursor, date_format_data_rows)

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
