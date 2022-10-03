"""Create Your Own Adventure: A Coin Flip Simulator."""

__author__ = "730487405"


import random

points: int = 0
player: str = ""
result: str = ""
n: int = 0
SMILE: str = "\U0001F603"
COIN: str = "\U0001FA99"
MONEY: str = "\U0001F4B0"
MONEY_FACE: str = "\U0001F911"


def main() -> None:
    """The main entrypoint of the game."""
    greet()
    user_input: str = input("How do you wish to begin? You can start the game by typing 'game', check your money by typing 'money', or quit by typing 'leave'. ")
    if user_input == "game":
        game()
    if user_input == "money":
        point_check(n)
    if user_input == "leave":
        goodbye()


def greet() -> None:
    """Welcomes the player into the game."""
    global player 
    player = input("What is your name? ")
    print(f"Welcome, {player}! This game will simulate a coin toss. Your objective is to guess the outcome of each coin flip. \n For each guess you get correct, you get another dollar. \n However, if you get one wrong, you lose all the money! \n Good luck!")


def game() -> None:
    """Allows players to check their guessing capabilities."""
    guess: str = input(f"{player}, please type 'Heads' or 'Tails' to indicate your guess for the coin flip. ")
    print("Nice guess! Let's see if you were correct.")
    result = random.choice(["Heads", "Tails"])
    check: str = (f"The result was: {result} {COIN}")
    print(check)
    if guess == result:
        global n 
        n += 1
        output: str = input(f"Wow, you're really great at this! You won $1 {MONEY}. Type 'Y' to play again or 'N' to cash out. You can also check your total awards accumulated by typing 'money'. ")
        if output == 'Y':
            game()
        if output == 'N':
            goodbye()
        if output == 'money':
            point_check(n)
    else:
        print(f"Sorry {player}! You guessed incorrectly.")
        n = 0
        goodbye()


def point_check(money: int) -> int:
    """Checks a players' money accumulated."""
    print("Money you've accumulated:")
    return n


def goodbye() -> None:
    """Bids farewell to our player."""
    print(f"You won ${n} {MONEY_FACE}. Play again soon {SMILE}!")


if __name__ == "__main__":
    main()