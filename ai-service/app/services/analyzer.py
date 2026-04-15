import json
import re
from app.services.gemini_client import call_gemini
from app.services.sentiment import sentiment_score


def extract_json(text: str):
    """
    Extract valid JSON from AI response safely
    """
    try:
        return json.loads(text)
    except:
        pass

    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass

    # fallback if parsing fails
    return {
        "sentiment_score": 0,
        "fraud_risk": 0.5,
        "trust_score": 50,
        "summary": "Failed to parse AI response",
        "recommendation": "neutral"
    }


def analyze_product(name, description, reviews):
    """
    Main AI product analysis pipeline
    """

    # ✅ 1. Local sentiment analysis
    sentiment = sentiment_score(reviews)

    # ✅ 2. Build AI prompt
    prompt = f"""
You are an expert AI product analyst.

Analyze the following product:

Name: {name}
Description: {description}
Reviews: {reviews}

Local Sentiment Score: {sentiment}

Return ONLY valid JSON in this format:

{{
  "sentiment_score": float,
  "fraud_risk": float,
  "trust_score": float,
  "summary": "short analysis",
  "recommendation": "buy" | "avoid" | "neutral"
}}
"""

    # ✅ 3. Call AI with SAFE handling
    try:
        ai_response = call_gemini(prompt)

        # 🔥 NEW: detect API error inside response (VERY IMPORTANT)
        if isinstance(ai_response, str) and '"error"' in ai_response.lower():
            raise Exception("AI returned error response")

        parsed = extract_json(ai_response)

    except Exception as e:
        # 🔥 fallback if API fails (quota / model / network)
        parsed = {
            "sentiment_score": sentiment,
            "fraud_risk": 0.5,
            "trust_score": 50,
            "summary": "AI unavailable, fallback used",
            "recommendation": "neutral"
        }

        ai_response = str(e)

    # ✅ 4. Final structured response
    return {
        "product_name": name,
        "sentiment_score": sentiment,
        "analysis": parsed,
        "raw_ai_response": ai_response
    }