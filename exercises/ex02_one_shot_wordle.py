"""EX02 - One Shot Wordle."""

__author__ = "730487405"

secret: str = "python"
word: str = input(f"What is your {len(secret)}-letter guess? ")
while len(word) != len(secret):
    word: str = input(f"That was not {len(secret)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

count: int = 0
emojis: str = ""
anywhere: bool = False
all_indices: int = 0

while count < len(secret):
    if word[count] == secret[count]:
        emojis: str = emojis + GREEN_BOX
    else:
        while anywhere != True and all_indices < len(secret):
            if word[count] == secret[all_indices]:
                anywhere: bool = True
            else:
                all_indices: int = all_indices + 1
        if anywhere == True:
            emojis: str = emojis + YELLOW_BOX
        else:
            emojis: str = emojis + WHITE_BOX
    count: int = count + 1
    anywhere: bool = False
    all_indices: int = 0

print(emojis)
if len(word) == len(secret):
    if word == secret:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")
