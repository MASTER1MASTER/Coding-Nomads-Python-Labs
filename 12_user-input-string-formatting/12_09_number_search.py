# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


user_input = int(input())



current_number = 0 

while current_number != user_input:
    current_number += 1

print("found it:", current_number)