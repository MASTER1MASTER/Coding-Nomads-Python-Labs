# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

user_string = str(input("Input a string here:"))

user_symbol = str(input("Now input a symbol to replace the first letter of the sting with:"))

first_letter = user_string[0]

modified_string = user_string.replace(first_letter, user_symbol)

print(modified_string)