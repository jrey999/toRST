import argparse


parser = argparse.ArgumentParser(
    description="""
    =====================
    CSV to RST converter
    =====================

    Converts CSV files to reStructuredText grids.

    Positional Arguments:
    csv_files               One or more CSV files to convert  

    Optional Arguments:
    -o, --output_dir        Output directory for RST files

    Example usage:

    torst mydata.csv mydata2.csv -o output/

    This will generate mydata.rst and mydata2.rst in the output folder.
    """
)
parser.add_argument(
    "files", nargs="+", help="""
    Positional Arguments
    --------------------

    files
    One or more files to convert. Multiple files can be specified separated  
    by spaces. The path can be absolute or relative to the current working
    directory.

    - *Type:* String
    - *Required:* Yes
    """
)

parser.add_argument(
    "-o", "--output_dir", default=".", help="""
    Optional Arguments:

    -o, --output_dir
    Output directory for generated RST files. Defaults to the current 
    working directory if not provided.
    """
)

def get_file_name(file: str) -> str:

    return file.split("/")[-1].split(".")[0]
