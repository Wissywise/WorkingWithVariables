

# Declaring the total grocery amount

total_grocery_budget = 55.00

# Prices of grocery items
apple_price = 10.00
orange_price = 15.00
banana_price = 20.00

#Tax rate charged on the purchase
TAX_RATE = 0.05

# Calculate the subtotal of the purchase items and the tax based on the subtotal
subtotal = apple_price + orange_price + banana_price

subtotal_tax = subtotal * TAX_RATE

# Total to pay for grocery shopping
total_price = subtotal + subtotal_tax

# The amount remaining after shopping
remaining_budget = total_grocery_budget - total_price


print(f"Total tax paid on grocery: £{subtotal_tax: .2f}")
print(f"Remaining budget: £{remaining_budget: .2f}")