 #create a simple calculator that determines the price of a meal after tax and tip.
# Declare the initial cost of the meal
meal = 44.50

# Convert the tax percentage to decimal
tax = 6.75 / 100

# Convert the tip percentage to decimal
tip = 15.0 / 100

# Calculate the cost after adding tax
meal += meal * tax

# Calculate total including tip
total = meal + meal * tip

# Output the total amount to pay, formatted to 2 decimal places
print(f"Total amount to pay: ${total:.2f}")