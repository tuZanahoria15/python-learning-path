# DYNAMIC ARGUMENTS
# Order matters - api_key is a required parameter, *args is optional and can take multiple values
def examples_args(api_key, *args):
    """Print an API key followed by its positional arguments.

    Demonstrate how *args captures additional positional
    arguments as a tuple after the required parameter.

    Args:
        api_key (str): The API key to display.
        *args: Additional positional arguments to print
            alongside their type.

    Examples:
        >>> examples_args("KEY", "a", "b")
        API Key: KEY
        ARGS: ('a', 'b')
        TYPE ARGS: <class 'tuple'>
        =====
    """
    print(f"API Key: {api_key}")
    print(f"ARGS: {args}")
    print(f"TYPE ARGS: {type(args)}")
    print("=====")


# Calling the function with different number of arguments to demonstrate *args
examples_args("API_KEY_VALUE", "This", "parameter", "here")
examples_args("API_KEY_VALUE", "Hello", "World")


"""
CODE QUALITY SECTION:
Usage of kwargs for dynamic keyword arguments in functions.
"""


# By convention, **kwargs is used to handle named arguments that are not predefined in the function signature.
def example_kwargs(**kwargs):
    """Print keyword arguments and their type.

    Demonstrate how **kwargs captures named arguments
    as a dictionary when no explicit parameters are defined.

    Args:
        **kwargs: Arbitrary keyword arguments to display.

    Examples:
        >>> example_kwargs(api_key="DEMO", timeout=30)
        KWARGS: <class 'dict'>
        KWARGS: {'api_key': 'DEMO', 'timeout': 30}
        =====
    """
    print(f"KWARGS: {type(kwargs)}")
    print(f"KWARGS: {kwargs}")
    print("=====")


# Calling the function
# The function can even work with different sets of keyword arguments.
example_kwargs(
    api_key="DEMO",
    query="Python News",
    timeout=30,
    retries=3,
)
example_kwargs(
    api_key="DEMO_GUARDIAN",
    query="Sports",
    from_date="2024-01-01",
    timeout=30,
    retries=3,
)