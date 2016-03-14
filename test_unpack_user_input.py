"""Verify the correct return size, order, and values for the
unpack_user_input() function in the find_user module.
"""
import find_user
import find_users_by_nationality

def test_find_user():
    """Test expected input, return order, and tuple size for the
    function unpack_user_input.
    """
    # Expected input.
    assert find_user.unpack_user_input(['database.sqlite', 'coit125']) == ('database.sqlite',
                                                                           'coit125')

    # Check return order.
    assert find_user.unpack_user_input(['database.sqlite', 'coit125']) != ('coit125',
                                                                           'database.sqlite')

    # Check tuple size.
    assert len(find_user.unpack_user_input(['database.sqlite', 'coit125'])) == 2

def test_find_users_by_nationality():
    """Test expected input, return order, and tuple size for the
    function unpack_user_input.
    """
    # Expected input.
    assert find_users_by_nationality.unpack_user_input(['database.sqlite',
                                                        'american']) == ('database.sqlite',
                                                                         'american')

    # Check return order.
    assert find_users_by_nationality.unpack_user_input(['database.sqlite',
                                                        'american']) != ('american',
                                                                         'database.sqlite')

    # Check tuple size.
    assert len(find_users_by_nationality.unpack_user_input(['database.sqlite', 'american'])) < 4
    assert len(find_users_by_nationality.unpack_user_input(['database.sqlite', 'american'])) > 1

    # Check nationalities larger than 1 word.
    assert find_users_by_nationality.unpack_user_input(['database.sqlite',
                                                        'south',
                                                        'korea']) == ('database.sqlite',
                                                                      'south korea')
