"""Verify if the function parse_date_parts() correctly parses and
returns a valid month, day, and year of a date from a given string.
"""
import birthdate

def test_parse_date_parts():
    """Assert correct return order and values of the parse_date_parts()
    function.
    """
    # Expected input.
    assert birthdate.parse_date_parts('01/25/1984') == ('1', '25', '1984')
    # Check months with 31 days.
    assert birthdate.parse_date_parts('01/31/1984') == ('1', '31', '1984')
    # Check months with 30 days.
    assert birthdate.parse_date_parts('11/30/1983') == ('11', '30', '1983')
    # Check February.
    assert birthdate.parse_date_parts('02/28/1980') == ('2', '28', '1980')
    # Check return order.
    assert birthdate.parse_date_parts('01/25/1984') != ('25', '1', '1984')
    # Check irregular input.
    assert birthdate.parse_date_parts('what?11/07/1983really!?') == ('11', '7', '1983')
