"""Verify if the function make_int converts a number in string form
into a number in integer form and returns it. If the string does not
contain a number, verify that the functions returns None.
"""
import date_validation

def test_make_int():
    """Assert the correct return of an integer or None for the function
    make_int given a number in string form.
    """
    # Expected input.
    assert date_validation.make_int('1') == 1
    # Check non-number string
    assert date_validation.make_int('one') is None
    # Check float number string
    assert date_validation.make_int('1.1') is None
