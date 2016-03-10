"""This module contains the getter functions shared by the find_user
modules.
"""
import re
import sys
import date_validation

def get_username(data_object, position):
    """Take in a data object and an integer representing a position in
    that data object. Get a username from the data object according to
    the position provided. Assert that the username is valid and return
    it.
    """
    assert isinstance(position, int), "An integer is needed for the position."
    username = data_object[position].lower()
    assert re.search(r"[\w.-]+", username), "Username not valid."
    return username

def get_nationality(data_object, position):
    """Take in a data object and an integer representing a position in
    that data object. Get a nationality from the data object according
    to the position provided. Assert that the nationality is valid and
    return it.
    """
    assert isinstance(position, int), "An integer is needed for the position."
    nationality = data_object[position].lower()
    assert re.search("[a-zA-Z]+ ?[a-zA-Z]*", nationality), "Nationality not valid."
    return nationality

def get_birthdate(data_object, birthdate_position, format_position):
    """Take in a data_object and get a birthdate from it. Assert that
    the elements of the birthdate are valid. Format the elements
    according to the structure found in the data_object. Return the
    formatted birthdate as a string.
    """
    assert isinstance(birthdate_position, int), "An integer is needed for the birthdate_position."
    assert isinstance(format_position, int), "An integer is needed for the format_position."
    month, day, year = date_validation.parse_date(data_object[birthdate_position])
    assert date_validation.is_valid_date(int(month), int(day), int(year)), "Birthdate not valid."
    return data_object[format_position].format(month=month, day=day, year=year).strip("'")

def get_db_filename(data_object, position):
    """Take in a data_object and an integer representing a position in
    that data object. Get a database filename from the data object
    according to the position provided. Assert that the database
    username is valid and return it.
    """
    assert isinstance(position, int), "An integer is needed for the position."
    db_filename = data_object[position].lower()
    assert re.search(r"[\w.-]+.sqlite", db_filename), "SQLite filename not valid."
    return db_filename

def get_cmd_ln_arguments(max_number, min_number):
    """Taken in two integers representing the upper_boundary amount of
    command line arguments to accept and the lower boundary amount of
    command line arguments to accept. Turn the arguments into a list
    and convert all of the items in the list to lowercase and return it.
    """
    assert isinstance(max_number, int), "An integer is needed for the max_number."
    assert isinstance(min_number, int), "An integer is needed for the min_number."
    raw_user_input = sys.argv[1:]
    user_input = [item.lower() for item in raw_user_input]
    assert len(user_input) <= max_number, "Too many arguments given."
    assert len(user_input) >= min_number, "Too few arguments given."
    return user_input
