"""EX05 - Unit Tests."""

__author__ = "730487405"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Ensures that the outputted list contains only even integers."""
    argument: list[int] = [1,2,3,4]
    i: int = 0
    output: list[int] = []
    while i < len(argument):
        if argument[i]%2 == 0:
            output.append(argument[i])
        i += 1
    assert output == [2,4]


def test_concat() -> None:
    """Checks the new list is a combination of the two arguments."""
    x: list[int] = [1,2,3]
    y: list[int] = [4,5,6]
    new_list: list[int] = [1,2,3,4,5,6]
    assert new_list == x + y


def test_sub() -> None:
    """Tests the outcome is the indices of the arguments."""
    a_list: list[int] = [1,2,3]
    a: int = 0
    z: int = len(a_list)-1
    outcome: list[int] = [1,3]
    assert outcome == [a_list[a], a_list[z]]