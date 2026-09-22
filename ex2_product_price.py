
#Show the Python code that stores the product details in variables using proper naming conventions

product_name = "Rice Cooker"

shelf_price = 760

tax_rate = 0.20

#Show the Python code that calculates the final price after adding tax.
tax_charged = float(shelf_price * tax_rate)

final_price = shelf_price + tax_charged

#Show the Python code that displays the formatted output with all details.

print(f" The product purchased is: {product_name} ")

print(f"The shelf price of the {product_name} is : {shelf_price} ")

print(f"The tax to pay on the purchased price is: {tax_charged}")

print(f"The final cost of the {product_name} is: {final_price}")