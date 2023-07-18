import csv


def from_csv(file) -> list[list]:

    """
    Read CSV file into a list of lists.

    Takes a CSV file path, opens the file, and returns the 
    contents parsed into a list of rows, where each row 
    is a list of the data cells.

    :param file: Path to CSV file
    :type file: str
    :returns: Parsed CSV data
    :rtype: list[list]
    """

    with open(file, mode="r") as f:
        csv_file = csv.reader(f)
        data=[row for row in csv_file]
    return data
