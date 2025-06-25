from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm() -> ChatOpenAI:
    """
    Returns the configured LLM instance.
    
    This function allows for easy access to the LLM instance throughout the application.
    It can be extended to include additional configuration or logging if needed.
    
    Returns:
        ChatOpenAI: The configured LLM instance.
    """
    return ChatOpenAI(model="gpt-3.5-turbo", 
                      temperature=0.7)