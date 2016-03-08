"""Verify if the function find_user() correctly finds a given user in a
given database.
"""
from find_user import find_user

def test_find_user():
    """Assert the correct return values of find_user() when given
    different username values to be found in the database.
    """
    db_filename = 'test_database.sqlite'
    template = """username: %s
nationality: %s
birthdate: %s"""
    # Check mm/dd/yyyy style user.
    assert find_user('coit125', db_filename) == template % ('coit125',
                                                            'american',
                                                            '1/25/1984')
    # Check dd/mm/yyyy style user.
    assert find_user('bcummberbatch', db_filename) == template % ('bcummberbatch',
                                                                  'british',
                                                                  '21/4/1978')
    # Check yyyy/mm/dd style user.
    assert find_user('orangelover1107', db_filename) == template % ('orangelover1107',
                                                                    'south korean',
                                                                    '1983/11/7')
    # Check case-sensitivity.
    assert find_user('COIT125', db_filename) == template % ('coit125',
                                                            'american',
                                                            '1/25/1984')
    # Check non-user.
    assert find_user('margesimpson', db_filename) == "Error, user not found."

    # Check no input.
    assert find_user('', db_filename) == "Error, user not found."

    # Check white space.
    assert find_user(' ', db_filename) == "Error, user not found."
