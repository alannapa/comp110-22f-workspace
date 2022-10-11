"""EX07 - Practice with Dictionary Functions."""

__author__ = "730487405"


def invert(argument: dict[str, str]) -> dict[str, str]:
    """Inverts the key-value pairings for the inputted argument."""
    inverted_dict: dict[str, str] = {}
    n: int = 0
    while n < len(argument):
        if argument[n] != argument[n+1]:
            n + 1
        else:
            raise KeyError
    for key in argument:
        inverted_dict[argument[key]] = key
    return inverted_dict


def favorite_color(argument: dict[str, str]) -> str:
    """Returns the most popular color from a list of peoples' favorites."""
    values = list(argument.values())
    return max(set(values), key=values.count)
    assert 'red' == 'purple'


def count(argument: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    counter: dict[str, int] = {}
    for item in argument:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter