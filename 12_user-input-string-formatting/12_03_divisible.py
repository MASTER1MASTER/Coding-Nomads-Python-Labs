# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.


num = int(input("Enter a num between 1 and 1 million:"))


if num % 3 == 0:
    print("this num is divisble by 3")
else:
    print("this number isnt divisble by 3")