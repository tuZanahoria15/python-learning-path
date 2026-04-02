"""Application configuration and constants."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"