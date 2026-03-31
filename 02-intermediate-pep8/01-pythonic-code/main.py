# main.py - All the code in a single file for simplicity

"""
Newsletter Analyzer System with multiple APIs
"""

# PEP 8: Centralized Configuration - Constants at the top and in UPPERCASE with underscores
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "en"  # PEP 8: Double quotes for strings


# PEP 8: Project common utilities - Define functions using snake_case
def clean_text(text):
    # PEP 8: Keep indentation consistent (4 spaces) no tabs
    """Cleans the input text and normalizes whitespace."""  # PEP 8: Docstrings with triple double quotes
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Use dobule blank lines to separate functions logically
def validate_api_key(api_key):
    """Validates the provided API key right format."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Main functions - Grouped before the utilities
def fetch_news_from_api(api_name, query):
    """Fetches news articles from the specified API based on the query."""
    pass


def process_article_data(raw_data):
    """Processes raw article data and extracts relevant information."""
    pass


"""
CODE QUALITY SECTION:
Usage of *args for dynamic arguments in functions.
"""


# API N.2
def guardian_client(api_key, section, from_date, timeout=30, replies=3):
    return f"Guardian {section} from {from_date} with timeout {timeout}"


# DYNAMIC ARGUMENTS
# Order matters - api_key is a required parameter, *args is optional and can take multiple values
def examples_args(api_key, *args):
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

API_KEY = "948a1310738140a59f74fb160f80aa6d99"
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
    """
    Flexible function to connect with the API
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
