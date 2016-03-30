"""Extract a valid username from a string."""
import re
from parse import parse

def get_from_label(username_str):
    """Take in a string containing a user's username in the format:
    username: <username>
    If a valid username is found after parsing, return it. Otherwise,
    return None.
    """
    username = parse(r"(username:)(?P<username>[\w.-]+)",
                     'username',
                     username_str,
                    )
    return username

def is_valid(username_str):
    """Take in a string containing a user's username. Return
    True if it is valid, None if it is not.
    """
    return True if re.search(r"[\w.-]+", username_str) else False
