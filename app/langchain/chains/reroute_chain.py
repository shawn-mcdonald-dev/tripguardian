from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain.chat_models.base import BaseChatModel

system_msg = """
You are TripGuardian, a helpful travel disruption assistant.

A user is experiencing a travel issue:
- Departure: {origin}
- Arrival: {destination}
- Delay: {delay_minutes} minutes
- Weather: {weather_conditions}
- User Priority: {user_priority}

Based on this, give a helpful, personalized recommendation for what the user should do next.

If the disruption is severe, suggest rebooking or a nearby hotel. If not, explain why they should wait.

Be friendly but direct. Offer 1-2 options.
"""


def suggest_reroute(data: dict, llm: BaseChatModel) -> str:
    """
    Run the reroute chain with user input.

    Parameters:
        data: dict with:
            - origin
            - destination
            - delay_minutes
            - weather_conditions
            - user_priority

    Returns:
        str: AI-generated recommendation
    """

    # Define the prompt template
    template = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", "Please help the user decide the best next step.")
    ])

    # Build a chain: prompt -> llm
    reroute_chain: Runnable = template | llm
    
    # Invoke OpenAI API for final response
    response = reroute_chain.invoke(data)
    return response.content.strip()

"""
Example usage:

response = reroute_chain.run({
    "origin": "JFK",
    "destination": "LHR",
    "delay_minutes": 150,
    "weather_conditions": "snowstorm",
    "user_priority": "minimize cost"
})
"""