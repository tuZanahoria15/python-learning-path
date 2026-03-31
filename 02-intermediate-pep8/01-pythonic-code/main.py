# main.py - All the code in a single file for simplicity

"""
Newsletter Analyzer System with multiple APIs
"""

# PEP 8: Centralized Configuration - Constants at the top and in UPPERCASE with underscores
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "en"  # PEP 8: Double quotes for strings


# PEP 8: Keep indentation consistent (4 spaces) no tabs
# PEP 8: Project common utilities - Define functions using snake_case
def clean_text(text):
    """Clean the input text and normalize whitespace.

    Strip leading and trailing whitespace from the input text
    and convert all characters to lowercase. Return an empty
    string if the input is falsy.

    Args:
        text (str): The raw text to be cleaned. Can be None
            or an empty string.

    Returns:
        str: The cleaned text in lowercase with no leading or
            trailing whitespace. Returns an empty string if
            the input is falsy.

    Raises:
        AttributeError: If `text` is a non-string type that
            does not implement `.strip()` or `.lower()`
            (e.g., int, list).

    Examples:
        >>> clean_text("  Hello World  ")
        'hello world'

        >>> clean_text("PYTHON")
        'python'

        >>> clean_text("")
        ''

        >>> clean_text(None)
        ''

        >>> clean_text("  Already Clean ")
        'already clean'
    """
    # PEP 257: Docstrings with triple double quotes
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Use double blank lines to separate functions logically
def validate_api_key(api_key):
    """Validate that an API key has the correct format.

    Check that the key is longer than 10 characters and
    contains only alphanumeric characters.

    Args:
        api_key (str): The API key string to validate.

    Returns:
        bool: True if the key is alphanumeric and longer than
            10 characters, False otherwise.

    Examples:
        >>> validate_api_key("abc123def456")
        True

        >>> validate_api_key("short")
        False

        >>> validate_api_key("has spaces !!")
        False
    """
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Main functions - Grouped before the utilities
def fetch_news_from_api(api_name, query):
    """Fetch news articles from the specified API.

    Placeholder function intended to retrieve articles
    matching the given query from a named API source.

    Args:
        api_name (str): Identifier of the target API
            (e.g., "newsapi", "guardian").
        query (str): The search term to look up.

    Returns:
        None: Not yet implemented.
    """
    pass


def process_article_data(raw_data):
    """Process raw article data and extract relevant fields.

    Placeholder function intended to transform raw API
    responses into a clean, structured format.

    Args:
        raw_data (dict): The unprocessed article data
            returned by an API client.

    Returns:
        None: Not yet implemented.
    """
    pass


"""
CODE QUALITY SECTION:
Usage of *args for dynamic arguments in functions.
"""


# API N.2
def guardian_client(api_key, section, from_date, timeout=30, replies=3):
    """Build a Guardian API request summary string.

    Simulate a connection to The Guardian API by returning
    a formatted string with the request parameters.

    Args:
        api_key (str): The Guardian API authentication key.
        section (str): News section to query (e.g., "world").
        from_date (str): Start date filter in "YYYY-MM-DD"
            format.
        timeout (int): Request timeout in seconds.
            Defaults to 30.
        replies (int): Maximum number of retry attempts.
            Defaults to 3.

    Returns:
        str: A formatted summary of the simulated request.

    Examples:
        >>> guardian_client("key123", "tech", "2024-01-01")
        'Guardian tech from 2024-01-01 with timeout 30'
    """
    return f"Guardian {section} from {from_date} with timeout {timeout}"


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

# This import is necessary to load environment variables from a .env file
# Which is a common practice for managing sensitive information like API keys without hardcoding them in the source code.
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

# Importing necessary libraries for making HTTP requests and handling URLs
import json
import urllib.parse
import urllib.request


# New custom class for handling specific errors
class NewSystemError(Exception):
    """A general error has occurred in the application."""

    pass


class APIKeyError(NewSystemError):  # Heredity goes between ()
    """An error has occurred related to API key issues."""

    pass


# STARTING SIMULATION: Mock API clients for demonstration purposes
# API N.1
def newsapi_client(api_key, query, timeout=30, retries=3):
    """Fetch articles from the NewsAPI service.

    Build a query URL, send an HTTP request to NewsAPI, and
    return the parsed JSON response as a dictionary.

    Args:
        api_key (str): NewsAPI authentication key.
        query (str): The search term to look up.
        timeout (int): Request timeout in seconds.
            Defaults to 30.
        retries (int): Maximum number of retry attempts.
            Defaults to 3.

    Returns:
        dict: Parsed JSON response containing articles and
            metadata from the NewsAPI service.

    Raises:
        APIKeyError: If the API responds with an HTTPError,
            indicating an invalid or expired API key.

    Examples:
        >>> newsapi_client("valid_key", "Python")
        {'status': 'ok', 'articles': [...]}
    """
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            # Bites data to string using decode() method
            data = response.read().decode("utf-8")
            return json.loads(data)  # Loads the content from the server in a dictionary
    except urllib.error.HTTPError:
        print("ERROR: The API KEY is invalid.")
        raise APIKeyError("An error has occurred: API connection failed.")
    return f"NewsAPI: {query} with timeout {timeout}"


# High priority parameters first, then optional or dynamic at the end
def fetch_news(api_name, *args, **kwargs):
    """Route a news request to the appropriate API client.

    Merge a base configuration with any provided keyword
    arguments, look up the matching client function by name,
    and delegate the call.

    Args:
        api_name (str): Identifier of the target API.
            Supported values: "newsapi", "guardian".
        *args: Positional arguments forwarded to the
            selected API client.
        **kwargs: Keyword arguments merged with the base
            config and forwarded to the client. Overrides
            defaults for "timeout" (30) and "retries" (3).

    Returns:
        dict | str: The response from the selected API
            client. Type depends on which client is called.

    Raises:
        TypeError: If `api_name` does not match any
            registered client, causing a NoneType call.

    Examples:
        >>> fetch_news("newsapi", api_key="key", query="AI")
        {'status': 'ok', 'articles': [...]}

        >>> fetch_news("guardian", "key", "tech", "2024-01-01")
        'Guardian tech from 2024-01-01 with timeout 30'
    """

    # Base Configuration that works across all APIs
    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    # **Merge base config with dynamic kwargs
    config = {
        **base_config,
        **kwargs,
    }

    # New API dictionary
    api_clients = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    # Select the client based on the api_name
    client = api_clients.get(api_name)
    return client(*args, **config)


# Handling the response and printing article titles
# Starting with response_data as None to ensure it is defined even if an exception occurs
response_data = None
try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python programming")
except APIKeyError as e:
    print(f"{e}")

# Checking if response_data is not None before trying to access its content
if response_data:
    for article in response_data["articles"]:
        print(article["title"])
