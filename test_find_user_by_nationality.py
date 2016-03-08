"""Verify if the function find_user_by_nationality() correctly returns
every user of a given nationality.
"""
from find_user_by_nationality import find_user_by_nationality

def test_find_user_by_nationality():
    """Assert the correct list of users returned from the database when
    the function find_user_by_nationality is given various
    nationalities as input.
    """
    db_filename = 'test_database.sqlite'
    error_msg = 'Error, no users of that nationality were found.'

    # Check database for a nationality with 1 user.
    assert find_user_by_nationality('south korean', db_filename) == ['orangelover1107']

    # Check database for a nationality with multiple users.
    assert find_user_by_nationality('american', db_filename) == ['coit125', 'austinwiltshire']

    # Check database for a nationality with 0 users.
    assert find_user_by_nationality('gondorian', db_filename) == [error_msg]

    # Check case-sensitivity.
    assert find_user_by_nationality('BRITISH', db_filename) == ['bcummberbatch']

    # Check no input.
    assert find_user_by_nationality('', db_filename) == [error_msg]

    # Check white space.
    assert find_user_by_nationality(' ', db_filename) == [error_msg]
