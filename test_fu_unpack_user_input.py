"""Verify the correct return size, order, and values for the
unpack_user_input() function in the find_user module.
"""
from find_user import unpack_user_input

def test_fu_unpack_user_input():
    """Test expected input, return order, and tuple size for the
    function unpack_user_input.
    """
    # Expected input.
    assert unpack_user_input(['database.sqlite', 'coit125']) == ('database.sqlite', 'coit125')

    # Check return order.
    assert unpack_user_input(['database.sqlite', 'coit125']) != ('coit125', 'database.sqlite')

    # Check tuple size.
    assert len(unpack_user_input(['database.sqlite', 'coit125'])) == 2
