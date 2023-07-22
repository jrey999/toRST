from funcs.funcs import handle_file, handle_raw


class Table:

    def __init__(self, input) -> None:
        
        self.data = handle_file(input) if isinstance(input, str) else handle_raw(input)
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
            max_width = max([len(str(row[index])) for row in self.data])
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
            "header": "+{}+".format("+".join([column_width * "=" for column_width in self.column_widths.values()])),
            "new_line": "+{}+".format("+".join([column_width * "-" for column_width in self.column_widths.values()]))
        }
    
    def build_table(self) -> list[str]:
        
        """
        Construct the reST grid table.

        This iterates through the data rows, building each line 
        of the table with proper column widths and formatting.

        :returns: A list of table lines
        :rtype: list[str]
        """
        table = [
            self.page_info["new_line"],
            "|{}|".format("|".join([str(cell) + " " * (self.column_widths[index] - len(str(cell))) for index, cell in enumerate(self.data[0])])),
            self.page_info["header"]
            ]
        for row in self.data[1:]:
            
            rst_row=[]
            for index, cell in enumerate(row):
                rst_row += [str(cell) + " " * (self.column_widths[index] - len(str(cell)))]
            table += ["|{}|".format("|".join(rst_row))] + [self.page_info["new_line"]]
        return "\n".join(table)