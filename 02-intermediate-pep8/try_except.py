# This allows us to use DivisionError as a custom exception in our codE.
class DivisionError(Exception):
    """An error has occurred during division operations."""

    pass


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

    if b == 2:
        # Raising a custom exception with a specific message
        raise DivisionError("Calculations with 2 are not allowed.")
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Print from finally block.")

print("This will always be printed, even if an exception occurs.")
