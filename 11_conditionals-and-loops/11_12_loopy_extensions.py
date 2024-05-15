# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

is_pdf = True  # Assume true and prove false if any check fails

# Define the expected extension in the correct order to compare from the end of the filename
expected_extension = ['f', 'd', 'p', '.']  # Note the order is reversed

# The number of characters in the expected extension
extension_length = len(expected_extension)

# Start checking from the end of the filename
for i in range(extension_length):
    # Compare each character from the end of the filename to the expected extension
    # We use negative indexing starting from -1 and going backwards
    if filename[-i-1] != expected_extension[i]:
        is_pdf = False
        break

if is_pdf:
    print("This is a pdf")
else:
    print("Not a pdf")