"""Demonstrates asking the user for input."""
#docstring is used to put a note about the contents of our file.
user_name: str = input("What is your name? ")
#we are going to store a variable, in this case the input to ask for our name and instead call that command 'user_name' to shorten it.
print("Hello, " + user_name + ", good morning!")
#print will produce the words inside of the quotation marks. there is a command inside the function that prompts for the user to put in their information.
print("You are awesome, " + user_name)
#since we stored the variable, the program will only ask us one time for our name and then insert the answer where there is 'user_name'.
