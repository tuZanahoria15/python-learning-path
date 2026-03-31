"""
Docstrings explained:

- Docstrings are string literals that appear right after the definition of a function, method, class, or module. They are used to document the purpose and usage of the code they describe.
"""


# Plain examples
def example_without_docstring():
    print("Hi, developer!")


def example_with_docstring() -> str:
    """
    This function returns a greeting message.

    Returns:
        str: A greeting message.
    """
    return "Hello, welcome to the world of Python!"


# How to access the code documentation of a function from code:
print(
    example_without_docstring.__doc__
)  # __doc__ atribute will protect from modifying the docstring accidentally.

print(example_with_docstring.__doc__)


# help() function will show the docstring in a more readable format.
help(example_with_docstring)


print("=====")


# Correct usage of docstrings
def correct_docstring_example(api_key: str, query: str) -> str:
    """
    DESCRIPTION:
    Fetches news articles from the specified API based on the query.

    ARGS:
        api_key (str): The API key for authentication.
        query (str): The search query for fetching news articles.

    RETURNS:
        str: A message indicating the result of the operation.

    EXCEPTIONS:
        ValueError: If the API key is invalid or the query is empty.

    EXAMPLES: (optional)
        >>> correct_docstring_example("VALID_API_KEY", "Python News")
        'Fetched news for query: Python News using API key: VALID_API_KEY'
    """
    return f"Fetched news for query: {query} using API key: {api_key}"
