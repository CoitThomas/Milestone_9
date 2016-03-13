"""Verify if the function are_valid_date_parts correctly determines the
validity of given integer representations of a date.
"""
import birthdate

def test_are_valid_date_parts():
    """Assert correct validation for various integer inputs to the
    function are_valid_date_parts.
    """
    # Expected input.
    assert birthdate.are_valid_date_parts(1, 25, 1984)
    # Check month
    assert not birthdate.are_valid_date_parts(-1, 25, 1984)
    assert not birthdate.are_valid_date_parts(13, 25, 1984)
    # Check day
    assert not birthdate.are_valid_date_parts(1, 32, 1984)
    assert not birthdate.are_valid_date_parts(1, 0, 1984)
    assert not birthdate.are_valid_date_parts(4, 31, 1984)
    assert not birthdate.are_valid_date_parts(2, 30, 1984)
    # Check year
    assert not birthdate.are_valid_date_parts(1, 25, 198444)
    assert not birthdate.are_valid_date_parts(1, 25, -1)
