import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm() -> ChatOpenAI:
    """
    Returns a ChatOpenAI instance configured with OpenRouter.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set in environment")

    return ChatOpenAI(
        model="x-ai/grok-4-fast:free",
        temperature=0.7,
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1"
    )
