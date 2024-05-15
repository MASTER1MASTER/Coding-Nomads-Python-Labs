# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
from random import randint

def guess_the_number(max_tries=3):
    number = randint(1, 10)
    attempts = 0
    
    print("guess a number between 1 and 10")
    print(f"You have {max_tries} to guess")
    
    while attempts < max_tries:
        try:
            guess = int(input("Enter your guess:"))
            attempts += 1
            
            if guess < 1 or guess > 10:
                print("Please guess a number within the range 1 to 10.")
            elif guess < number:
                print("Too low, try again.")
            elif guess > number:
                print("Too high, try again.")
            else:
                print("Congratulations! You guessed the right number.")
                break  # Breaks the loop if the correct number is guessed
        except ValueError:
            print("Please enter a valid integer.")

        # Check if the maximum attempts have been reached
        if attempts == max_tries and guess != number:
            print(f"Sorry, you've used all your attempts. The number was {number}.")

guess_the_number()