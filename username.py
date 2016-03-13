"""Extract a valid username from a string."""
from parse import parse

def get(username_str):
    """Take in a string containing a user's username. If a valid
    username is found after parsing, return it. Otherwise, return None.
    """
    username = parse(r"(username:)?(?P<username>[\w.-]+)",
                     'username',
                     username_str,
                    )
    return username if username and username!='username' else None
