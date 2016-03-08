"""Verify if the function build_date() correctly parses and returns a
valid month, day, and year of a date from a given string.
"""
import date_validation

def test_parse_date():
    """Assert correct return order and values of the build_date()
    function.
    """
    # Expected input.
    assert date_validation.parse_date('01/25/1984') == ('1', '25', '1984')
    # Check months with 31 days.
    assert date_validation.parse_date('01/31/1984') == ('1', '31', '1984')
    # Check months with 30 days.
    assert date_validation.parse_date('11/30/1983') == ('11', '30', '1983')
    # Check February.
    assert date_validation.parse_date('02/28/1980') == ('2', '28', '1980')
    # Check return order.
    assert date_validation.parse_date('01/25/1984') != ('25', '1', '1984')
    # Check irregular input.
    assert date_validation.parse_date('what?11/07/1983really!?') == ('11', '7', '1983')
