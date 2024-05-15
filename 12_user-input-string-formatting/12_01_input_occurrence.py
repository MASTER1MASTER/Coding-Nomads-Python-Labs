# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#



user_string = input("Enter a string of words:")

user_letter = input("Enter a letter to fidn within this string:")


index = user_string.find(user_letter)

if user_letter in user_string:
    print(f"The first occurence of '{user_letter} is at '{index}'")
else:
    print("that is not in your string")
    