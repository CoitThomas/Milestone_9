"""Verify if the function is_valid_str_date correctly determines the
validity of a given string representations of a date in the format:
mm/dd/yyyy
"""
import date_validation

def test_is_valid_str_date():
    """Assert correct validation for various integer inputs for the
    function is_valid_str_date.
    """
    # Expected input.
    assert date_validation.is_valid_str_date('11/7/1983')
    # Check month boundaries.
    assert date_validation.is_valid_str_date('1/25/1984')
    assert date_validation.is_valid_str_date('12/25/1984')
    # Check day boundaries.
    assert date_validation.is_valid_str_date('1/31/1984')
    assert date_validation.is_valid_str_date('1/1/1984')
    assert date_validation.is_valid_str_date('2/28/1984')
    assert date_validation.is_valid_str_date('4/30/1984')
    # Check year boundaries.
    assert date_validation.is_valid_str_date('1/25/2200')
    assert date_validation.is_valid_str_date('1/25/1800')
