"""Test cases for dictionary functions."""

__author__ = "730487405"


from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Tests that the function inverts all key-value pairs."""
    argument: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(argument) == {'b': 'a', 'd': 'c'}


def test_invert_empty_argument() -> None:
    """Tests outcome when argument is incomplete."""
    argument: dict[str, str] = {'a'}
    assert invert(argument) == {'a'}


def test_invert_duplicate_keys() -> None:
    """Tests outcome when keys are duplicated."""
    argument: dict[str, str] = {'a': 'b', 'c': 'd', 'a': 'e'}
    assert invert(argument) == {'e': 'a', 'd': 'c'}


def test_count() -> None:
    """Tests that the function returns the frequency of strs."""
    argument: list[str] = ['a', 'a', 'a', 'b', 'b', 'c']
    assert count(argument) == {'a': 3, 'b': 2, 'c': 1}