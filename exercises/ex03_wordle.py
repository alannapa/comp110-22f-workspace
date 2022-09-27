"""EX03 - Structured Wordle."""

__author__ = "730487405"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    winner: bool = False
    secret: str = "sleep"
    while turns <= 6 and winner is not True:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        message: str = ""
        if guess == secret:
            winner = True
            message += (f"You won in {turns}/6 turns!")
        else:
            message += ("X/6 - Sorry, try again tomorrow!")
        turns += 1
    print(message)


def contains_char(word: str, letter: str) -> bool:
    """Given a string, check to see if the letter is contained within in."""
    assert len(letter) == 1
    count: int = 0
    match: bool = False
    while match is not True and count < len(word):
        if letter == word[count]:
            match = True
        else:
            count += 1
    return match


def emojified(secret: str, guess: str) -> str:
    """Returns colored boxes to give hints to user."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    output: str = ""
    counter: int = 0
    while counter < len(secret):
        if guess[counter] == secret[counter]:
            output += GREEN_BOX
        else:
            if contains_char(guess, secret[counter]):
                output += YELLOW_BOX
            else:
                output += WHITE_BOX
        counter += 1
    return output


def input_guess(expected: int) -> str:
    """Makes the user guess a word the same length as the secret word."""
    prompt: str = input(f"Enter a {expected} character word: ")
    while expected != len(prompt):
        prompt = input(f"That wasn't {expected} chars! Try again: ")
    return prompt