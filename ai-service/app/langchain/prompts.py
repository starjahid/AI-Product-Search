PRODUCT_ANALYSIS_PROMPT = """
You are an expert product analyst AI.

Analyze the following product:

Product Name: {name}
Description: {description}
Reviews: {reviews}

Return JSON with:
- sentiment_score (0-1)
- fraud_risk (0-1)
- trust_score (0-100)
- summary (short)
- recommendation (buy / avoid / neutral)
"""