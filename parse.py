"""Parse a string into a desired string."""
import re

def parse(regex, group_name, string):
    """Take in a string. Parse the string according to a given
    regular expression. Group the parsed data according to a given
    group name and return it. If there is not a match, return None.
    """
    parsed_data = re.search(regex, string)
    return parsed_data.group(group_name) if parsed_data else None