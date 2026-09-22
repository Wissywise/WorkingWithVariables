
# Personal Budget Calculator

# Get income from the user
main_income = int(input("Enter your total monthly income (in $): "))
other_income = int(input("Enter your other monthly income (in $): "))

# Calculate the total income from the user
total_income = main_income + other_income

# Get expenses from the user
rent = int(input("Enter your rent expense (in $): "))
groceries = int(input("Enter your groceries expense (in $): "))
transport = int(input("Enter your transport expense (in $): "))
utilities = int(input("Enter your utilities expense (in $): "))
other_expenses = int(input("Enter your other expenses (in $): "))

# Calculate total expenses
total_expenses = rent + groceries + transport + utilities + other_expenses

# Calculate remaining budget
remaining_budget = total_income - total_expenses

# Display results
print(f"Total Income:  $", round(total_income, 2))
print(f"Total Expenses: ${total_expenses:.2f}")
print("Remaining Budget: ",f"${remaining_budget:.2f}")