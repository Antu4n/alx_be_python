income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income-expenses
print(f"Your monthly savings are ${savings}.")
projected_savings = (savings * 12 + (savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
