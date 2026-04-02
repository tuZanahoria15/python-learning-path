import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# From OPENAI documentation available at https://github.com/openai/openai-python
def analyze_news_with_ai(articles: list[dict], query: str) -> str | None:

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Creating context for the AI to analyze the news articles
    context = "\n".join(
        f"- {article['title']}: {article.get('description', '')[:100]}..."
        for article in articles [:10] # Limiting to the first 10 articles for costs management
    )

    # Creating a prompt for the AI to analyze the news articles based on the query
    prompt = f"""
        Based on the following news articles:
        {context}

        Question: {query}

        Please provide a concise answer in English.
    """

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are an agent that reads context and answers questions brefily.",
        input=prompt,
    )

    print(response.output_text)