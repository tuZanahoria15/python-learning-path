# Using f-strings for string interpolation
# Useful for constructing messages, URLs, or any string that requires variable substitution

from datetime import datetime

name = "Fer"
year = 2003
age = 23
text = f"Hello, {name}! Welcome to the Python learning path."  # Using f-string for string interpolation
print(text)

text_sum = f"Hello, the sum is:  {1 + 4}"
print(text_sum)

text_age = f"Hello, {name}! your age is: {2026 - year} years old"
print(text_age)

text_func = f"Hello {name.upper()}!!"
print(text_func)

text_if = f"Hello {name}, you are {'an adult' if age >= 18 else 'a minor'}."
print(text_if)


# Old complex way to read and lower performance
text_format = "Hello, {}".format(name)
print(text_format)


print("=====")

bank_balance = 4500000
text_balance = f"Your current bank balance is: ${bank_balance:,}"  # This comma will format the number with a comma as a thousand separator
print(text_balance)

stock_price = 1.495
text_stock = f"The current stock price is: ${stock_price:.1f}"  # This will format the number to 1 decimal place
print(text_stock)

stock_price = 1.495
text_stock = f"The current stock price is: ${stock_price:.2f}"  # This will format the number to 2 decimal places
print(text_stock)

user_id = 1000
text_user = f"Your user ID is: {user_id:03d}"  # This will format the number adding leading zeros to make it 3 digits
print(text_user)

print("=====")

product = "Laptop"
price = 1000

# Using < or > to left-align or right-align the product name within a 10-character width
text = f"Product: {product:<10} | Price: ${price:>10}"
## Shows the text twice to see the alignment effect
print(f"{text}\n{text}")

print("=====")

# Common usage of f-strings
date = datetime(2024, 12, 5, 10, 10)

# ISO format: 2024-12-05T10:10:00
text_date = f"Current date and time: {date}"
print(text_date)

# Full weekday name and day of the month: Thursday 05
text_date = f"Current date and time: {date: %A %d}"
print(text_date)
