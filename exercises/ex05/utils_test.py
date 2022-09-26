"""EX05 - Unit Tests."""

__author__ = "730487405"


from utils import only_evens, sub, concat


def test_only_evens_1() -> None:
    """Ensures that the outputted list contains only even integers."""
    argument_1: list[int] = [1, 2, 3, 4]
    i: int = 0
    output: list[int] = []
    while i < len(argument_1):
        if argument_1[i] % 2 == 0:
            output.append(argument_1[i])
        i += 1
        return output
    assert only_evens == [2, 4]


def test_only_evens_2() -> None:
    """Tests what happens when negative numbers are in the list."""
    argument_2: list[int] = [-1, -2, -3]
    j: int = 0
    output: list[int] = []
    while j < len(argument_2):
        if argument_2[j] % 2 == 0:
            output.append(argument_2[j])
        j += 1
        return output
    assert only_evens == [-2]


def test_only_evens_3() -> None:
    """Tests when argument is an empty list."""
    argument_3: list[int] = []
    k: int = 0
    output: list[int] = []
    while k < len(argument_3):
        if argument_3[k] % 2 == 0:
            output.append(argument_3[k])
        k += 1
        return output
    assert output == []


def test_concat_1() -> None:
    """Checks results when the lists are different integers, same length."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    n: int = 0
    new_list_1: list[int] = []
    while n < len(x):
        new_list_1.append(x[n])
        n += 1
    n = 0
    while n < len(y):
        new_list_1.append(y[n])
        n += 1
    return new_list_1
    assert concat == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    """Checks the results when one list is empty."""
    x2: list[int] = [1, 2, 3]
    y2: list[int] = []
    n2: int = 0
    new_list: list[int] = []
    while n2 < len(x2):
        new_list.append(x2[n2])
        n2 += 1
    n2 = 0
    while n2 < len(y2):
        new_list.append(y2[n2])
        n2 += 1
    return new_list
    assert concat == [1, 2, 3]


def test_concat_3() -> None:
    """Checks the result when the lists are the same integers and the same lengths."""
    x3: list[int] = [1, 2, 3]
    y3: list[int] = [1, 2, 3]
    n3: int = 0
    new_list_3: list[int] = []
    while n3 < len(x3):
        new_list_3.append(x3[n3])
        n3 += 1
    n3 = 0
    while n3 < len(y3):
        new_list_3.append(y3[n3])
        n3 += 1
    return concat == [1, 2, 3, 1, 2, 3]


def test_sub_1() -> None:
    """Tests the outcome is the indices of the arguments."""
    a_list_1: list[int] = [10, 20, 30, 40]
    a: int = 0
    z: int = 4
    if len(a_list_1) == 0 or a >= len(a_list_1) or z <= 0:
        return []
    if a < 0:
        a = 0
    if z > len(a_list_1):
        z = len(a_list_1)
    outcome: list[int] = []
    z -= 1
    outcome.append(a_list_1[a])
    outcome.append(a_list_1[z])
    return outcome
    assert sub == [10, 40]


def test_sub_2() -> None:
    """Tests the results when the first index variable is negative."""
    a_list_2: list[int] = [10, 20, 30, 40]
    a2: int = -1
    z2: int = 3
    if len(a_list_2) == 0 or a2 >= len(a_list_2) or z2 <= 0:
        return []
    if a2 < 0:
        a2 = 0
    if z2 > len(a_list_2):
        z2 = len(a_list_2)
    outcome: list[int] = []
    z2 -= 1
    outcome.append(a_list_2[a2])
    outcome.append(a_list_2[z2])
    return outcome
    assert sub == [10, 30]


def test_sub_3() -> None:
    """Tests the results when the second argument index is out of range."""
    a_list_3: list[int] = [10, 20, 30, 40]
    a3: int = 0
    z3: int = 5
    if len(a_list_3) == 0 or a3 >= len(a_list_3) or z3 <= 0:
        return []
    if a3 < 0:
        a3 = 0
    if z3 > len(a_list_3):
        z3 = len(a_list_3)
    outcome: list[int] = []
    z3 -= 1
    outcome.append(a_list_3[a3])
    outcome.append(a_list_3[z3])
    return outcome
    assert sub == [10, 40]