""""""
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

while count < len(secret):
    if word[count] == word[secret]:
        emojis: emojis + GREEN_BOX
    else:
        emojis: emojis + WHITE_BOX
    count = count + 1

print(emojis)
if len(word) == len(secret):
    if word == secret:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")