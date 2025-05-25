monthly_income = int(input("Enter your monthly income: "))
# This script calculates the monthly savings of a person based on their income and expenses.
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # Assuming we want to project savings for a year with 5% interest

# Display the result
print("Monthly savings are", monthly_savings)

# Display the projected savings
print("Projected savings after one year, with interest is:", projected_savings)
