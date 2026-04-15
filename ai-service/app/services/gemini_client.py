import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def call_gemini(prompt: str):

    if not OPENROUTER_API_KEY:
        return "OPENROUTER_API_KEY not found in environment"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Product Search"
    }

    payload = {
        # ✅ SAFE WORKING MODEL
        "model": "openai/gpt-3.5-turbo",

        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(URL, headers=headers, json=payload)

        # 🔥 DEBUG HELP (VERY IMPORTANT)
        if response.status_code != 200:
            return {
                "error": response.text,
                "status_code": response.status_code
            }

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"OpenRouter Exception: {str(e)}"