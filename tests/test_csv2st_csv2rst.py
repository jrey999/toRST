from csv2rst.csv2rst import Table
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