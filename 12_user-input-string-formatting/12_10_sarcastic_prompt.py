# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_input = str(input("Spit some shit nigger:"))


def sarcastic_txt(input_text):
    result_text = ""
    use_upper = True  # Start with uppercase
    for char in input_text:
        if char.isalpha():  # Check if the character is a letter
            if use_upper:
                result_text += char.upper()
            else:
                result_text += char.lower()
            use_upper = not use_upper  # Toggle between upper and lower case
        else:
            result_text += char  # Add non-alphabet characters unchanged

    return result_text

# Getting user input
user_input = input("Spit some shit playa: ")

# Transforming the input to sarcastic text
sarcastic_output = sarcastic_txt(user_input)

# Printing the transformed output
print(sarcastic_output)

