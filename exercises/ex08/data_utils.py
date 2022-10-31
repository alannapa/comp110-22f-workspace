"""Dictionary related utility functions."""

__author__ = "730487405"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a roww-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    if n > len(column_table):
            return column_table
    for column in column_table:
        a_list: list[str] = []
        i: int = 0
        while i < n:
            a_list.append(column_table[column][i])
            i += 1
        result[column] = a_list
    return result


def select(column_table: dict[str, list[str]], a_list: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in a_list:
        result[column] = column_table[column]
    return result


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two tables combined."""
    result: dict[str, list[str]] = {}
    for column in column_table_one:
        result[column] = column_table_one[column]
    for column in column_table_two:
        if column in result:
            result[column] += column_table_two[column]
        else:
            result[column] = column_table_two[column]
    return result


def count(a_list: list[str]) -> dict[str, int]:
    """Counts the number of apperances a key makes in a list."""
    result: dict[str, int] = {}
    for item in a_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result