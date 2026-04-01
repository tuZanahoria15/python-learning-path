"""
Typing with Python: Type Hints and Annotations
"""

from typing import Any

variable = 42  # Int Variable
print(f"Variable: {variable}, Type: {type(variable)}")

# Next line will cause an error when Mypy is enabled, because we are trying to assign a string to an integer variable.
# variable = "Testing text"
print(f"Variable: {variable}, Type: {type(variable)}")

# Adding type hints to a function definition
# variable: type = value
new_variable: int = 44
print(f"New Variable: {new_variable}, Type: {type(new_variable)}")

print("=====")

# | is used to indicate that a variable can be of multiple types (Union)
user_id: int | None = None  # This variable can be either an integer or None


"""
Example of type hints for parameters and return type.
"""


# Typing a function with type hints for parameters
def sum(a: int, b: int):
    """This function takes two integers and returns their sum."""
    return a + b


# Typing another functiion with a return type hint
def sum_numbers(a: int, b: int) -> int:
    """This function takes two integers and returns their sum."""
    return a + b


# This list is typed to contain only dictionaries
articles: list[dict] = [
    {"title": "Example"},
    {"title": "Example 2"},
]

# This list is typed to contain only lists of strings
articles_two: list[list][str] = [
    ["item", "others"],
    ["item", "others 2"],
]

# Any is a special type hint that indicates that a variable can be of any type.
# But it is generally recommended to use more specific type hints whenever possible to improve code readability and maintainability.
articles_three: list[list][Any] = [
    ["item", "others"],
    ["item", "others 2"],
]

# int, str, list, dict, tuple, Any
