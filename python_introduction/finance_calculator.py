# Enter your monthly income
# Enter your total monthly expenses
# Simple annual interest rate = 0.05
# Calculate the monthly savings by substracting monthly expenses from the monthly income

# monthly savings = monthly income - monthly expenses
# Annual savings = monthly savings * 12 * (1 + 0.05)

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12 * (1 + 0.05)



# simple annual interest rate = 0.05
print(f"projected savings {annual_savings}, ")
