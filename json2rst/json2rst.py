import json


def from_json(file) -> list[list]:

    data=json.load(open(file, "r"))
    if isinstance(data, dict):
        raise ValueError("JSON must be list of lists or list of dicts")
    elif isinstance(data, list):
        if isinstance(data[0], list):
            return data
        else:
            return [[key for key in data[0].keys()]] + [list(_.values()) for _ in data]