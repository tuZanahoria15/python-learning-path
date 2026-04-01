"""Common utility functions for the project."""


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