from csv2rst.csv2rst import from_csv
from json2rst.json2rst import from_json


def get_extension(file: str) -> str:

    return file.split(".")[-1].lower()

def handle_file(file: str) -> list[list]:

    extension = get_extension(file)
    if extension == "csv":
        return from_csv(file)
    elif extension == "json":
        return from_json(file)
    else:
        raise ValueError(f"{extension} files not currently supported")