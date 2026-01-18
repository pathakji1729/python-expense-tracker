print("Expense Tracker - Day 3")

# Take input from user
amount = int(input("Enter expense amount: "))
description = input("Enter expense description: ")

# Open file in append mode
file = open("expenses.txt", "a")

# Write expense to file
file.write(f"{amount},{description}\n")

# Close the file
file.close()

print("Expense saved successfully!")
