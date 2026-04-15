from langchain_core.prompts import PromptTemplate
from app.services.gemini_client import llm
from app.langchain.prompts import PRODUCT_ANALYSIS_PROMPT

def analyze_product_llm(name, description, reviews):

    prompt = PRODUCT_ANALYSIS_PROMPT.format(
        name=name,
        description=description,
        reviews=" | ".join(reviews)
    )

    response = llm.invoke(prompt)

    return response.content