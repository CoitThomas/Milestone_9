"""Verify if the function parse() correctly utilizes a given regex to
parse, group, and return desired information from a string.
"""
import parse

def test_parse():
    """Assert the correct return values when parse is called to parse,
    group and retun desired information from a string.
    """
    regex = "(?P<name>[a-zA-Z]+ ?[a-zA-Z]*)"
    assert parse.parse(regex, 'name', '07734 Hyewon Namkung') == 'Hyewon Namkung'
    assert not parse.parse(regex, 'name', '123450987*&!@#$')
