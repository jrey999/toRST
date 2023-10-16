import json


def from_list_values(data: dict[str, list]) -> list[list]:
    count, list_list = 0, [list(data.keys())] + [[] for value in data[list(data.keys())[0]]]
    for _ in data.values():
        count += 1
        for index, value in enumerate(_):
            
            list_list[index + 1].insert(count, value)
    return list_list

def from_json(file) -> list[list]:

    data=json.load(open(file, "r"))
    if isinstance(data, dict):
        for key, value in data.items():
            if not isinstance(key, str) and isinstance(value, list):
                raise ValueError("JSON must be list of lists or list of dicts")
            else:
                return from_list_values(data)
    elif isinstance(data, list):
        if isinstance(data[0], list):
            return data
        else:
            return [[key for key in data[0].keys()]] + [list(_.values()) for _ in data]