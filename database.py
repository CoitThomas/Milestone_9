"""Confirm the validity of and make queries on an sqlite database."""
import re

def is_valid_name(filename):
    """Take in a string, if it is a valid sqlite database filename,
    return True, otherwise, return None.
    """
    return re.search(r"\b[\w.-]+.sqlite\b", filename)

def query(select_statement, search_term, db_cursor):
    """Take in an SQL 'select_statement' as a string, a 'search_term' as
    a string, and an active 'db_cursor' object. Execute the query on
    the database and return the first result.
    """
    db_cursor.execute(select_statement, (search_term,))
    row = db_cursor.fetchone()
    return row

def query_all(select_statement, search_term, db_cursor):
    """Take in an SQL 'select_statement' as a string, a 'search_term' as
    a string, and an active 'db_cursor' object. Execute the query on
    the database and return a list of all of the results.
    """
    db_cursor.execute(select_statement, (search_term,))
    rows = db_cursor.fetchall()
    return rows
