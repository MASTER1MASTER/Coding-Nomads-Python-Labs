# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
import sys

while True:
    print("This is an infinite Loop///")
    
    user_input = input("Anything you would like to say about That?:")
    if user_input == "quit":
        sys.exit("Will DO!")
    
print("This line will not be printed if the loop is exited")