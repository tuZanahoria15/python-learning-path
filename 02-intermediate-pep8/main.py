"""Newsletter Analyzer System with multiple APIs."""

# Using "." to import from the news_analyzer package, to indicate that the module is part of the same package.
from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError
from news_analyzer.utils import get_unique_sources, get_articles_by_source, get_reading_time
from news_analyzer.open_ai import analyze_news_with_ai

# Starting with response_data as None to ensure it is defined even if an exception occurs
response_data = None
try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python programming")
except APIKeyError as e:
    print(f"{e}")

# Checking if response_data is not None before trying to access its content
if response_data:
    
    analyze_news_with_ai(response_data["articles"], query="What is your opinion on Python programming language?")

    # # Usage of enumerate to print unique sources with their index
    # sources_set =  get_unique_sources(response_data["articles"])
    # for index, source in enumerate(sources_set, start=1):
    #     print(f"No: {index} -- {source}")

    # articles = list(map(get_reading_time, response_data["articles"]))
    # for article in articles:
    #     print(f"{article['title']} - Estimated Reading Time: {article['reading_time']} minutes")

    # #for article in response_data["articles"]:
    #     #print(article["title"])

    # github_articles = get_articles_by_source(response_data["articles"], "github.com")
    # for github_article in github_articles:
    #     # Show the source name and title of each article from github.com
    #     print(github_article["source"]["name"], github_article["title"])

