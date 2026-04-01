"""Application configuration and constants."""
 
from dotenv import load_dotenv
import os
 
# PEP 8: Centralized Configuration - Constants at the top and in UPPERCASE with underscores
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "en"
 
# Load environment variables from .env file
load_dotenv()
 
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"