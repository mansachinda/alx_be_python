# Input Prompt for Monthly Income and Montly Expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculates Monthly Savings
Monthly_Savings = monthly_income - monthly_expenses

# Calculate Projected Annual Savings
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
Projected_Savings = int(Projected_Savings)

# Prints result of both outputs below
print(f"Your monthly savings are ${Monthly_Savings}. \nProjected savings after one year, with interest, is: ${Projected_Savings}.")
