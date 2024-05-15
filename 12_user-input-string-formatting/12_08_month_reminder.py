# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

months = ["january", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


user_num = int(input("enter a num between 1 & 12:"))

if user_num <= 12:
    index = user_num
    print(f"The correspoonding month for that number is {months[index-1]}")
else:
    print("That number is not between 1 andf 12")