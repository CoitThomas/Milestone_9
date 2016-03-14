"""Extract a valid birthdate from a string."""
import re
from parse import parse

def get_from_label(birthdate_str):
    """Take in a birthdate as a string"""
    birthdate = parse("(birthdate:)(?P<birthdate>[0-9]{1,2}/[0-9]{1,2}/[0-9]{4})",
                      "birthdate",
                      birthdate_str,
                     )
    if birthdate:
        assert is_valid(birthdate)
        return birthdate
    else:
        return None

def format_date(birthdate_str, template):
    """Take in a birthdate as a string and parse it into its parts.
    Rearrange the parts to fit into a given template and return the the
    newly formatted birthdate string.
    """
    assert is_valid(birthdate_str)
    month, day, year = parse_date_parts(birthdate_str)
    assert are_valid_date_parts(make_int(month), make_int(day), make_int(year))
    return template.format(month=month, day=day, year=year)

def is_valid(birthdate_str):
    """Take in a string representing a date in the format:
    mm/dd/yyyy
    Verify it is a valid representation and return True or False.
    """
    str_month, str_day, str_year = parse_date_parts(birthdate_str)
    month = make_int(str_month)
    day = make_int(str_day)
    year = make_int(str_year)
    return are_valid_date_parts(month, day, year)

def valid_month(month):
    """Take in an integer representing a month of the year. Return True
    if it is valid. Otherwise, return False.
    """
    return 1 <= month <= 12

def valid_day(day, month):
    """Take in an integer representing a day and month of the year.
    Return True if it is a valid day for the given month. Otherwise,
    return False.
    """
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    assert valid_month(month)
    if month in month31:
        return 1 <= day <= 31
    if month in month30:
        return 1 <= day <= 30
    if month == 2:
        return 1 <= day <= 28

def valid_year(year):
    """Take in an integer representing a pertinent year. Return True if
    it is valid. Otherwise, return False.
    """
    return 1900 <= year <= 2016

def are_valid_date_parts(month, day, year):
    """Take in three integers representing a month, day, and year.
    Verify they are valid representations and return True or False.
    """
    return valid_month(month) and valid_day(day, month) and valid_year(year)

def make_int(string):
    """Convert a given numerical string to an integer. If it cannot be
    converted, return None.
    """
    try:
        return int(string)
    except ValueError:
        return None

def parse_date_parts(string):
    """Take in a string containing a date in the format mm/dd/yyyy and
    return three numerical strings representing a valid day, month, and
    year.
    """
    date = re.search("(?P<month>[0-9]{1,2})" # Month.
                     "/(?P<day>[0-9]{1,2})" # Day.
                     "/(?P<year>[0-9]{4})", string) # Year.
    assert date, "A string in the format mm/dd/yyyy must be provided."

    month = make_int(date.group('month'))
    day = make_int(date.group('day'))
    year = make_int(date.group('year'))

    assert are_valid_date_parts(month, day, year), "A valid date must be provided."

    return str(month), str(day), str(year)
