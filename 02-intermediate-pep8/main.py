"""Newsletter Analyzer System with multiple APIs."""

from config import API_KEY
from exceptions import APIKeyError
from news_api_client import fetch_news

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