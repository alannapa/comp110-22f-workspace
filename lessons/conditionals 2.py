"""An example of conditional (if-else) statements."""
SECRET: int = 3
#our secret number is going to be 3.
print("I'm thinking of a number between 1-5, what is it?")
#this gives players the rules of our game.
guess: int = int(input("What is your guess? "))
#this asks them for their input to type in a number.

if guess == SECRET: 
#the function 'if' is a special code in python and can only be used for if-else statements.
    print("You guessed correctly!!!")
    #the output if they guess correctly is indented below the if function.
    print("Have a wonderful day!!!")
else:
#else is indented on the same line as 'if'.
    print("Sorry, you guessed incorrectly :(")
    #the output if they guess incorrectly is indented below the else function.
    if guess > SECRET:
        print("You guessed too high!")
        #we can put an if-else statement inside of another one that prompts the user to change their guess according to where it falls on the spectrum.
    else:
        print("You guessed too low!")
        #instead of writing an if-else for guessing too low, we can do the complement of guessing too high.
    print("Try running the program again.")
print("Game over.")
#the output if they guess incorrectly is at the same indentation as the if-else statement.
