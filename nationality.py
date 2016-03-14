"""Extract a valid nationality from a string."""
import re
from parse import parse

def get_from_label(nationality_str):
    """Take in a string containing the name of a nationality in the
    format:
    nationality: <nationality>
    If a valid nationality is found after parsing, return it. Otherwise,
    return None.
    """
    nationality = parse("(nationality:)(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*)",
                        "nationality",
                        nationality_str,
                       )
    return nationality if nationality else None

def get(nationality_str):
    """Take in a string containing the name of a nationality. If a
    valid nationality is found after parsing, return it. Otherwise,
    return None.
    """
    nationality = parse("(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*)",
                        "nationality",
                        nationality_str,
                       )
    return nationality if nationality else None

def is_valid(nationality_str):
    """Take in a string containing the name of a nationality. Return
    True if it is valid, None if it is not.
    """
    return re.search("[a-zA-Z]+ ?[a-zA-Z]*", nationality_str)
