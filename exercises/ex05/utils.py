"""EX05 - Skeleton function."""

__author__ = "730487405"


def only_evens(argument: list[int]) -> list[int]:
    """Returns only even numbers when given a list."""
    i: int = 0
    output: list[int] = []
    while i < len(argument):
        if argument[i] % 2 == 0:
            output.append(argument[i])
        i += 1
    return output


def concat(x: list[int], y: list[int]) -> list[int]:
    """Concatenates a new list from two lists."""
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


def sub_2(a_list: list[int], a: int, z: int) -> list[int]:
    """Returns a list as a subset of the given list."""
    i: int = 0
    output: list[int] = []
    if len(a_list) == 0 or a >= len(a_list) or z <= 0:
        return []
    if a < 0:
        a = 0
    if z > len(a_list):
        z = len(a_list)
    while i < len(a_list) and a < z:
        output.append(a_list[a])
        a += 1
    return output