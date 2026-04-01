"""API client functions for fetching news from multiple sources."""

import json
import urllib.parse
import urllib.request

from config import BASE_URL
from exceptions import APIKeyError


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
            # Bytes data to string using decode() method
            data = response.read().decode("utf-8")
            return json.loads(data)
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

    # Merge base config with dynamic kwargs
    config = {
        **base_config,
        **kwargs,
    }

    # API client registry
    api_clients = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    # Select the client based on the api_name
    client = api_clients.get(api_name)
    return client(*args, **config)