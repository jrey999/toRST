from toRST.toRST import Table
from csv2rst.csv2rst import clean_csv
from funcs.funcs import handle_raw
import pytest


@pytest.fixture
def empty_table():

    yield Table('tests/csv/empty.csv')

@pytest.fixture
def large_table():

    yield Table('tests/csv/large.csv')

@pytest.fixture
def small_table():

    yield Table('tests/csv/small.csv')

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
    assert str(value_error.value) == "input must be of type list[list] or list[dict]"

    with pytest.raises(ValueError) as value_error:
        handle_raw(["value", "value", "value", "value"])
    assert str(value_error.value) == "input must be of type list[list] or list[dict]"
