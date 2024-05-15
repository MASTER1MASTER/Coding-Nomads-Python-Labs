




days_worked = input("How many days did you work?;")

payment_due = int(days_worked) * 200

if days_worked:
    print("You are owed " + str(payment_due))
else:
    print("i need a number!")