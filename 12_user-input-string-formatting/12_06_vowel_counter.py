# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
vowels = "aeiou"

user_input = str(input("give me a string and i will tell you how many times each vowel appears:"))

for i in user_input:
    if i in vowels:
        counter = user_input.count(i)
        print(f"the vowel {i} appears {counter} times")
     