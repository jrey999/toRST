from funcs.funcs import get_extension
from csv2rst.csv2rst import from_csv
from json2rst.json2rst import from_json


def handle_file(file: str) -> list[list]:

    extension = get_extension(file)
    if extension == "csv":
        return from_csv(file)
    elif extension == "json":
        return from_json(file)
    else:
        raise ValueError(f"{extension} files not currently supported")
class Table:

    def __init__(self, file) -> None:
        
        self.data = handle_file(file)
        self.headers = self.data[0]
        self.column_widths = self.get_column_widths()
        self.page_info = self.get_page_info()

    

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