# Lists comprehensions are useful for creating new lists based on existing iterables.
# They provide a concise and readable way to generate lists in a single line of code.

from sample_data import sample_articles

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


print(extract_titles_traditional(sample_articles))
print("=====")
print(extract_titles_comprehension(sample_articles))
print("=====")
print(extract_article_summaries(sample_articles))


def get_sources_traditional(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


def get_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def categorize_traditional(articles):
    sources = get_sources(articles)
    results = {}

    for source in sources:
        if source not in results:
            results[source] = []

        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)

    return results


def categorize(articles):
    sources = get_sources(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize_traditional(sample_articles))
print("===")
print(categorize(sample_articles))
