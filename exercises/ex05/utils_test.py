"""EX05 - Unit Tests."""

__author__ = "730487405"


from utils import only_evens, sub, concat


def test_only_evens_1() -> None:
    """Ensures that the outputted list contains only even integers."""
    argument: list[int] = [1, 2, 3, 4]
    i: int = 0
    output: list[int] = []
    while i < len(argument):
        if argument[i] % 2 == 0:
            output.append(argument[i])
        i += 1
        return output
    assert output == [2, 4]


def test_only_evens_2() -> None:
    """Tests what happens when negative numbers are in the list."""
    argument: list[int] = [-1, -2, -3]
    i: int = 0
    output: list[int] = []
    while i < len(argument):
        if argument[i] % 2 == 0:
            output.append(argument[i])
        i += 1
        return output
    assert output == [-2]


def test_only_evens_3() -> None:
    """Tests when argument is an empty list."""
    argument: list[int] = []
    i: int = 0
    output: list[int] = []
    while i < len(argument):
        if argument[i] % 2 == 0:
            output.append(argument[i])
        i += 1
        return output
    assert output == []


def test_concat_1() -> None:
    """Checks results when the lists are different integers, same length."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    n: int = 0
    new_list: list[int] = []
    while n < len(x):
        new_list.append(x[n])
        n += 1
    n = 0
    while n < len(y):
        new_list.append(y[n])
        n += 1
    return new_list
    assert new_list == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    """Checks the results when one list is empty."""
    x: list[int] = [1, 2, 3]
    y: list[int] = []
    n: int = 0
    new_list: list[int] = []
    while n < len(x):
        new_list.append(x[n])
        n += 1
    n = 0
    while n < len(y):
        new_list.append(y[n])
        n += 1
    return new_list
    assert new_list == [1, 2, 3]


def test_concat_3() -> None:
    """Checks the result when the lists are the same integers and the same lengths."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [1, 2, 3]
    n: int = 0
    new_list: list[int] = []
    while n < len(x):
        new_list.append(x[n])
        n += 1
    n = 0
    while n < len(y):
        new_list.append(y[n])
        n += 1
    return new_list == [1, 2, 3, 1, 2, 3]


def test_sub_1() -> None:
    """Tests the outcome is the indices of the arguments."""
    a_list: list[int] = [10, 20, 30, 40]
    a: int = 0
    z: int = 4
    if len(a_list) == 0 or a >= len(a_list) or z <= 0:
        return []
    if a < 0:
        a = 0
    if z > len(a_list):
        z = len(a_list)
    outcome: list[int] = []
    z -= 1
    outcome.append(a_list[a])
    outcome.append(a_list[z])
    return outcome
    assert outcome == [10, 40]


def test_sub_2() -> None:
    """Tests the results when the first index variable is negative."""
    a_list: list[int] = [10, 20, 30, 40]
    a: int = -1
    z: int = 3
    if len(a_list) == 0 or a >= len(a_list) or z <= 0:
        return []
    if a < 0:
        a = 0
    if z > len(a_list):
        z = len(a_list)
    outcome: list[int] = []
    z -= 1
    outcome.append(a_list[a])
    outcome.append(a_list[z])
    return outcome
    assert outcome == [10, 30]


def test_sub_3() -> None:
    """Tests the results when the second argument index is out of range."""
    a_list: list[int] = [10, 20, 30, 40]
    a: int = 0
    z: int = 5
    if len(a_list) == 0 or a >= len(a_list) or z <= 0:
        return []
    if a < 0:
        a = 0
    if z > len(a_list):
        z = len(a_list)
    outcome: list[int] = []
    z -= 1
    outcome.append(a_list[a])
    outcome.append(a_list[z])
    return outcome
    assert outcome == [10, 40]