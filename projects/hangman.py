# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

# Initial setup
word = "devize"
frame = "_" * len(word)
attempts = 0
max_attempts = 6  # You can change this based on desired difficulty

print("""
Today we are playing hangman.
The description of the word is: a future billion dollar plus valued software development company.
The length of the word is: {}
""".format(frame))

# Main game loop
while "_" in frame and attempts < max_attempts:
    guess = input("Guess a letter: ").strip().lower()

    # Check if the guess is valid
    if guess.isalpha() and len(guess) == 1:
        if guess in word:
            # Find all occurrences of the guessed letter and update the frame
            frame = ''.join([guess if word[i] == guess else frame[i] for i in range(len(word))])
            print("Nice guess: ", frame)
        else:
            attempts += 1
            print(f"Wrong guess, try again. Attempts remaining: {max_attempts - attempts}")
    else:
        print("Invalid input, please guess a single alphabetic character.")

    # Check if the game is won
    if "_" not in frame:
        print("Congratulations! You've guessed the word correctly:", word)
        break

# Check if the game is lost
if attempts >= max_attempts:
    print("Sorry, you've run out of attempts. The word was:", word)