import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not GEMINI_API_KEY:
    print("[WARNING]: Gemini API Key is missing. Check your .env file setup!")

if not OPENAI_API_KEY:
    print("[WARNING]: OpenAI API Key is missing. Check your .env file setup!")