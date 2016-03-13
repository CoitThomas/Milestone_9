"""Extract a valid nationality from a string."""
from parse import parse

def get(nationality_str):
    """Take in a string containing the name of a nationality. If a
    valid nationality is found after parsing, return it. Otherwise,
    return None.
    """
    nationality = parse("(nationality:)?(?P<nationality>[a-zA-Z]+ ?[a-zA-Z]*)",
                        "nationality",
                        nationality_str,
                       )
    return nationality if nationality and nationality != 'nationality' else None
