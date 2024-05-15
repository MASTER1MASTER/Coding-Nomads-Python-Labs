# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


name = str(input("What is your name?:"))


name_split = name.split()[0]

print(f"hello {name_split}, its nice to meet you!")