"""Open a file, read in the data, divide the data into smaller
packages, and return them.
"""

def get_data(filename, package_size=1):
    """Take in a string 'filename' and an integer 'package_size'. Read in
    the data from the file and divide the data into chunks that are
    'package_size' number of lines each. Return a list containing the
    packages of data.
    """
    data = read_file(filename)
    assert data, "There is no data in file: %s" % filename
    return package_file_data(data, package_size)

def read_file(file_name):
    """Read in data from a file and return it."""
    with open(file_name, 'r') as some_file:
        data = some_file.read()
    return data

def package_file_data(file_data, package_size):
    """Take in data as a string and an integer 'package_size'. Return a
    list containing chunks of data that are 'package_size' number of
    lines each.
    """
    data_lines = file_data.splitlines()
    assert data_lines, "There is no data!"
    assert isinstance(package_size, int), "An integer must be provided."
    assert 0 < package_size <= len(data_lines), "A valid package size must be provided."
    assert len(data_lines) % package_size == 0, "Data is incomplete."
    return [data_lines[pos:pos + package_size] for pos in range(0, len(data_lines), package_size)]
