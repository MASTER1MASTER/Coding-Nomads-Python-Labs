# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


str_1 = str(input("write a string!:"))
str_2 = str(input("give me anotha:"))
str_3 = str(input("last one, one more:"))


longest_str = max (str_1, str_2, str_3, key=len)

len_of_longest = len(longest_str)

print(f"the longest string given was {longest_str}, and the lenght was {len_of_longest} characters long.")