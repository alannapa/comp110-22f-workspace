"""An example of a list utility algorithm."""

# Name: contains
# Function with 2 parameters;
#   needle - what we're searching for
#   haystack - what we're searching through
# Return Type: bool

# Start from first index
# Loop through each index of list
#   Test if equal to needle
#       Yes! Return True
# Return False

def contains (needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False

