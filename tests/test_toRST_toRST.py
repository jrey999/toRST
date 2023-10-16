from toRST.toRST import Table
from formats.csv2rst import clean_csv
from formats.json2rst import from_list_values
from funcs.funcs import handle_raw
import pytest, json


@pytest.fixture
def empty_table():

    yield Table('tests/data/empty.csv')

@pytest.fixture
def large_table():

    yield Table('tests/data/large.csv')

@pytest.fixture
def small_table():

    yield Table('tests/data/small.csv')

def test_headers(empty_table, large_table, small_table) -> None:

    assert empty_table.headers == ["No","Data","Here"]
    assert large_table.headers == ["First Name","Last Name","Job Title","Biography"]
    assert small_table.headers == ["Header1","Header2","Header3"]

def test_column_widths(empty_table, large_table, small_table) -> None:

    assert empty_table.column_widths[0] == len("No")
    assert large_table.column_widths[1] == len("Livingston")
    assert small_table.column_widths[2] == len("Header3")

def test_clean_csv() -> None:

    assert clean_csv([["ab", "cd", "ef", "gh", "", ""], ["ba", "dc", "fe", "hg", "", ""]]) == [["ab", "cd", "ef", "gh"], ["ba", "dc", "fe", "hg"]]

def test_handle_raw() -> None:

    with pytest.raises(ValueError) as value_error:
        handle_raw({"key1": "value1", "key2": "value2"})
    assert str(value_error.value) == "input must be of type list[list or dict or tuple] or dict[str, list]"

    with pytest.raises(ValueError) as value_error:
        handle_raw(["value", "value", "value", "value"])
    assert str(value_error.value) == "input must be of type list[list or dict or tuple] or dict[str, list]"

def test_int_headers() -> None:

    assert Table([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).headers == ["1", "2", "3"]

def test_from_list_values() -> None:
    data = json.load(open("tests/data/list_values.json"))
    assert from_list_values(data) == [
        ['height', 'weight', 'age', 'country'],
        [170.5, 70.4, 28, 'USA'],
        [180.3, 90.2, 32, 'Canada'],
        [176.8, 80.5, 31, 'UK'],
        [182.6, 75.3, 36, 'Australia']
        ]
