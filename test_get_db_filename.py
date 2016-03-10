"""Verify if the function get.db_filename() correctly returns a
database filename from a data object.
"""
import get

def test_get_db_filename():
    """Assert the correct return value for get.db_filename."""
    data_object = [1, 'a', 1.2, 'hello', 'world', 'test_database.sqlite', 'TEST_DATABASE.SQLITE']

    # Expected input.
    assert get.get_db_filename(data_object, 5) == 'test_database.sqlite'

    # Check capitalization.
    assert get.get_db_filename(data_object, 6) == 'test_database.sqlite'
