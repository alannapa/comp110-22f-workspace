"""EX05 - Unit Tests."""

__author__ = "730487405"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Ensures that the outputted list contains only even integers."""
    argument: list[int] = [1, 2, 3, 4]
    assert only_evens(argument) == [2, 4]


def test_only_evens_empty() -> None:
    """Tests when argument is an empty list."""
    argument: list[int] = []
    assert only_evens(argument) == []


def test_only_evens_negative() -> None:
    """Tests when the argument contains negative numbers."""
    argument: list[int] = [-1, -2, -3]
    assert only_evens(argument) == [-2]


def test_concat() -> None:
    """Checks results when the lists are different integers, same length."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_concat_empty() -> None:
    """Checks the results when both lists are empty."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_same() -> None:
    """Checks the result when the lists are the same integers and the same lengths."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [1, 2, 3]
    assert concat(x, y) == [1, 2, 3, 1, 2, 3]


def test_sub_empty() -> None:
    """Tests the outcome is the indices of the arguments when the list is empty."""
    a_list: list[int] = []
    a: int = 0
    z: int = 4
    assert sub(a_list, a, z) == []


def test_sub_negative() -> None:
    """Tests the results when the first index variable is negative."""
    a_list: list[int] = [10, 20, 30, 40]
    a: int = -1
    z: int = 3
    assert sub(a_list, a, z) == [10, 20, 30]


def test_sub_out_of_range() -> None:
    """Tests the results when the second argument index is out of range."""
    a_list: list[int] = [10, 20, 30, 40]
    a: int = 0
    z: int = 5
    assert sub(a_list, a, z) == [10, 20, 30, 40]