# Lists comprehensions are useful for creating new lists based on existing iterables.
# They provide a concise and readable way to generate lists in a single line of code.

sample_articles = [
    {
        "title": "Breaking News: Python Takes Over the World",
        "source": {"name": "Tech Times"},
        "description": "Big news in the tech world",
        "category": "Technology",
    },
    {
        "title": "Sports Update: Local Team Wins Championship",
        "source": {"name": "Sports Daily"},
        "description": "Exciting finish in the championship game",
        "category": "Sports",
    },
    {
        "title": "Health Tips: How to Stay Fit During Winter",
        "source": {"name": "Health Weekly"},
        "description": "Stay healthy with these winter fitness tips",
        "category": "Health",
    },
    {
        "title": "Entertainment: New Movie Release Breaks Box Office Records",
        "source": {"name": "Entertainment News"},
        "description": "The latest blockbuster is a hit",
        "category": "Entertainment",
    },
    {
        "title": "Business Insights: Market Trends to Watch",
        "source": {"name": "Business Insider"},
        "description": "Key market trends for investors",
        "category": "Business",
    },
    {
        "title": "Science Discoveries: New Planet Found in Our Solar System",
        "source": {"name": "Science Daily"},
        "description": "A new planet has been discovered",
        "category": "Science",
    },
]


# Extracting titles using a traditional for loop
def extract_titles_traditional(articles):
    """Extracts only the titles using a traditional for loop."""
    titles = []
    for article in articles:
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


# Extracting titles using a list comprehension
def extract_titles_comprehension(articles):
    """Extracts only the titles using a list comprehension."""
    return [article["title"] for article in articles if len(article["title"]) > 10]


# Extracting article summaries using a dictionary comprehension
def extract_article_summaries(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 20
    }


# Extracting unique sources using a traditional for loop
def get_sources_traditional(articles):
    # Set() structure will automatically handle duplicates
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


# Extracting sources using a set comprehension
def get_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


# print(extract_titles_traditional(sample_articles))
print("=====")
# print(extract_titles_comprehension(sample_articles))
print("=====")
# print(extract_article_summaries(sample_articles))
print("=====")
# print(get_sources_traditional(sample_articles))
print("=====")
# print(get_sources(sample_articles))


# Traditional way to categorize articles by source
def categorize_articles(articles):
    sources = get_sources(articles)
    results = {}

    for source in sources:
        if source not in results:
            results[source] = []

        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)
    return results


print(categorize_articles(sample_articles))


# Comprehension way to categorize articles by source
def categorize_articles_comprehension(articles):
    sources = get_sources(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize_articles_comprehension(sample_articles))
