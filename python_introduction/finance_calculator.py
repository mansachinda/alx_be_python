# Input Prompt for Monthly Income and Montly Expenses
mi = input("Enter your monthly income: ")
i = int(mi)
me = input("Enter your total monthly expenses: ")
e = int(me)

# Calculates Monthly Savings
ms = i - e

# Calculate Projected Savings
projected_savings = ms * 12 + (ms * 12 * 0.05)
ps = int(projected_savings)

# Prints result of both outputs below
print("Your monthly", "savings are", "$",ms)
print("Projected savings after one year, with interest, is:", "$",ps)
