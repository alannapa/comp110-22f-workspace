"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730487405"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)
letter_one: str = word[0]
letter_two: str = word[1]
letter_three: str = word[2]
letter_four: str = word[3]
letter_five: str = word[4]
count: int = 0
if letter == letter_one:
    print(letter + " found at index 0")
    count = count + 1
if letter == letter_two:
    print(letter + " found at index 1")
    count = count + 1
if letter == letter_three:
    print(letter + " found at index 2")
    count = count + 1
if letter == letter_four:
    print(letter + " found at index 3")
    count = count + 1
if letter == letter_five:
    print(letter + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + letter + " found in " + word)
if count == 1:
    print("1 instance of " + letter + " found in " + word)
if count == 2:
    print("2 instances of " + letter + " found in " + word)
if count == 3:
    print("3 instances of " + letter + " found in " + word)
if count == 4:
    print("4 instances of " + letter + " found in " + word)
if count == 5:
    print("5 instances of " + letter + " found in " + word)