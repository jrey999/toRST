import csv


def clean_csv(data: list[list]):
    """
    Removes trailing empty strings from CSVs that ovvur when extra commas exist
    
    :param data: list of lists returned from from_csv function
    :type data: list of lists
    :rtype: list[list]
    """
    while data[0][-1] == "":
        for _ in data:
            _.pop()
    return data

def from_csv(file: str) -> list[list]:

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

    with open(file) as f:

        csv_file = csv.reader(f)
        data = [row for row in csv_file]
    return clean_csv(data)
