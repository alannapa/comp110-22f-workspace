"""EX04 - Working with lists."""

__author__ = "730487405"

def all(haystack: list[int], needle: int) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            i += 1
        else:
            return False
    return True


def max(argument: list[int]) -> int:
    if len(argument) == 0:
        raise ValueError("max() arg is an empty List")
    n: int = 1
    while n < len(argument):
        if argument[n] > argument[0]:
            n += 1
            if argument[n] > argument [1]:
                return argument[n]
            else:
                return argument [1]
        else:
            n += 1
            if argument [n] > argument [0]:
                return argument [n]
            else: return argument[0]


def is_equal(first: list[int], second: list[int]) -> bool:
    a: int = 0
    while a < len(first) and len(second):
        if first[a] == second[a]:
            a += 1
        else:
            return False
    return True