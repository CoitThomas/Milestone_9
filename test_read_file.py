"""Verify if the function read_file() correctly reads and returns the
information found in a text file.
"""
from read_file import read_file

def test_read_file():
    """Assert the correct return value from the function read_file()."""
    assert read_file('test_read_file.txt') == """ABCDEFGHIJKLMNOPQRSTUVWXYZ?
abcdefghijklmnopqrstuvwxyz.
"""
