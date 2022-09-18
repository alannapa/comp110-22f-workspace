"""EX04 - Working with lists."""

__author__ = "730487405"


def all(haystack: list[int], needle: int) -> bool:
    """Checks if one character is the same as the entire list."""
    i: int = 0
    if len(haystack) == 0:
        return False
    while i < len(haystack):
        if haystack[i] == needle:
            i += 1
        else:
            return False
    return True


def max(argument: list[int]) -> int:
    """Finds the maximum of a list without using max function."""
    if len(argument) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = argument[0]
    n: int = 1
    while n < len(argument):
        if argument[n] > max_value:
            max_value = argument[n]
        else:
            n += 1
    return max_value


def is_equal(first: list[int], second: list[int]) -> bool:
    """Checks that two lists match each other exactly."""
    output: bool = True
    a: int = 0
    while a < len(first) or len(second):
        if first[a] == second[a]:
            a += 1
        else:
            return False
    return True