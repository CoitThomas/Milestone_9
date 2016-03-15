"""Extract a valid date_format from a string."""
import re
from parse import parse

def get(date_format_str):
    """Take in a string with a date format style in the form:
    {word}/{word}/{word}
    If it matches an american, european, or chinese style date format,
    return the format, otherwise, return None.
    """
    american_style = "{month}/{day}/{year}"
    european_style = "{day}/{month}/{year}"
    chinese_style = "{year}/{month}/{day}"
    date_format = parse("(?P<date_format>((" +
                        re.escape(american_style) + ")|(" +
                        re.escape(european_style) + ")|(" +
                        re.escape(chinese_style) + ")))",
                        "date_format",
                        date_format_str,
                       )
    return date_format
