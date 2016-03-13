"""Verify the correct return size, order, and values for the
unpack_user_input() function in the find_users_by_nationality module.
"""
from find_users_by_nationality import unpack_user_input

def test_fubn_unpack_user_input():
    """Test expected input, return order, and tuple size for the
    function unpack_user_input.
    """
    # Expected input.
    assert unpack_user_input(['database.sqlite', 'american']) == ('database.sqlite', 'american')

    # Check return order.
    assert unpack_user_input(['database.sqlite', 'american']) != ('american', 'database.sqlite')

    # Check tuple size.
    assert len(unpack_user_input(['database.sqlite', 'american'])) < 4
    assert len(unpack_user_input(['database.sqlite', 'american'])) > 1

    # Check nationalities larger than 1 word.
    assert unpack_user_input(['database.sqlite', 'south', 'korea']) == ('database.sqlite',
                                                                        'south korea')
