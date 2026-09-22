
# Temperature Conversion Program

# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit, '°F')

# Input temperature in Fahrenheit
fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", celsius, '°C')

print('-----------------------------------------------------------------')

# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}°F")

# Input temperature in Fahrenheit
fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9
print(f"Temperature in Celsius: {celsius}°C")