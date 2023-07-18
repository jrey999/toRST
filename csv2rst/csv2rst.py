import csv


class Table:

    def __init__(self, file) -> None:
        
        self.data = self.get_list(file)
        self.headers = self.data[0]
        self.column_widths = self.get_column_widths()
        self.page_info = self.get_page_info()

    def get_list(self, file) -> list[list]:

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

    def get_column_widths(self) -> dict[int, int]:
        """
        Get the maximum width for each column.
        
        This determines the column widths needed to properly 
        format the reStructuredText grid by finding the max
        string length in each column of data.

        :returns: A dictionary with column index as key and width as value
        :rtype: dict[int, int]
    """
        column_widths = {}
        for index in range(int(len(self.headers))):
            max_width = max([len(row[index]) for row in self.data])
            column_widths[index] = max_width if max_width > len(self.headers[index]) else len(self.headers[index])
        return column_widths

    def get_page_info(self) -> dict[str, int or str]:
        """
        Get formatting information for the reST page.

        This returns a dictionary containing:

        - Number of columns
        - Total page width 
        - Separator string

        :returns: Dict with page formatting metadata
        :rtype: dict[str, int or str]
        """
        return {
            "num_columns": len(self.headers),
            "page_wdith": sum(self.column_widths.values()),
            "new_line": "".join(["+" + column_width * "=" for column_width in self.column_widths.values()]) + "+"
        }
    
    def build_table(self) -> list[str]:
        
        """
        Construct the reST grid table.

        This iterates through the data rows, building each line 
        of the table with proper column widths and formatting.

        :returns: A list of table lines
        :rtype: list[str]
        """
        table = []
        for row in self.data:
            
            table += [self.page_info["new_line"]]
            rst_row=""
            for index, cell in enumerate(row):
                column_width = self.column_widths[index]
                rst_row += "|" + (cell + " " * (column_width - len(cell)))
            table += [rst_row + "|"]
        return table + [self.page_info["new_line"]]