
# Declaring the total grocery amount

total_grocery_budget = float(input("\nEnter total grocery budget amount: "))

# Prices of grocery items
apple_price = float(input("\nEnter Price of apple: "))
orange_price = float(input("\nEnter Price of orange: "))
banana_price = float(input("\nEnter Price of banana: "))

#Tax rate charged on the purchase
tax_rate = float(input("\nEnter tax rate: "))

# Calculate the subtotal of the purchase items and the tax based on the subtotal
subtotal = apple_price + orange_price + banana_price

subtotal_tax = subtotal * tax_rate

# Total to pay for grocery shopping
subtotal_price = subtotal + subtotal_tax

# The amount remaining after shopping
remaining_budget = total_grocery_budget - subtotal_price

print(f"\nTotal grocery budget: £{total_grocery_budget:.2f}")
print(f"Total grocery purchased: £{subtotal_price:.2f}")
print(f"Total before Tax: £{subtotal:.2f}")
print(f"Total tax paid on grocery: £{subtotal_tax:.2f}")
print(f"Remaining budget: £{remaining_budget:.2f}")
