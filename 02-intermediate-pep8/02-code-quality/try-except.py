"""
How to know the type of an exception and handle it accordingly:
Assigning the exception to a variable (e)
allows us to access its message and type,
which can be useful for debugging and providing
more informative error messages to the user.

SINTAX:
try:
    # Code that may raise an exception
except Exception as e:
    print(f"E: {e}, Type: {type(e)}")
"""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
