from csv2rst.csv2rst import from_csv
from json2rst.json2rst import from_json, from_list_values


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

def handle_raw(input: list[list or dict]) -> list[list]:

    if not isinstance(input, list) or isinstance(input, dict):
        raise ValueError("input must be of type list[list or dict or tuple] or dict[str, list]")
    else:
        if isinstance(input[0], list):
            return input
        elif isinstance(input[0], dict):
            return [[key for key in input[0].keys()]] + [list(row.values()) for row in input[1:]]
        elif isinstance(input[0], tuple):
            return [list(row) for row in input]
        elif isinstance(input, dict) and isinstance(list(input.values())[0], list):
            return from_list_values(input)
        else: raise ValueError("input must be of type list[list or dict or tuple] or dict[str, list]")