"""Extract desired information from a string using a given regular
expression.
"""
import re

def parse(regex, group_name, string):
    """Take in a string. Parse the string according to a given
    regular expression. Group the parsed data according to a given
    group name and return it. If there is not a match, return None.
    """
    parsed_data = re.search(regex, string)
    if parsed_data:
        return parsed_data.group(group_name)
    return None
