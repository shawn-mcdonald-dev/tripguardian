import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
BASE_URL = "http://api.aviationstack.com/v1/flights"


def get_flight_status(flight_number: str, flight_date: str) -> dict:
    """
    Get real-time flight status using AviationStack API.

    Parameters:
        flight_number (str): e.g., "AA100"
        flight_date (str): ISO format date, e.g., "2025-06-13"

    Returns:
        dict: status, delay, departure/arrival info
    """
    airline_code = ''.join(filter(str.isalpha, flight_number))
    flight_no = ''.join(filter(str.isdigit, flight_number))

    params = {
        "access_key": AVIATIONSTACK_API_KEY,
        "flight_iata": flight_number,
        "flight_date": flight_date
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        flights = data.get("data", [])
        if not flights:
            return {"error": "Flight not found or not operating on this date."}

        flight = flights[0]
        return {
            "airline": flight["airline"]["name"],
            "flight_number": flight["flight"]["iata"],
            "departure_airport": flight["departure"]["airport"],
            "arrival_airport": flight["arrival"]["airport"],
            "scheduled_departure": flight["departure"]["scheduled"],
            "status": flight["flight_status"],
            "delay_minutes": flight["departure"].get("delay", 0)
        }

    except Exception as e:
        return {"error": str(e)}

def get_sample_flight_status(flight_number: str, flight_date: str) -> dict:
    """
    Get sample flight status from a local JSON file for testing/demo purposes.

    Parameters:
        flight_number (str): e.g., "AA100"
        flight_date (str): ISO format date, e.g., "2025-06-13"

    Returns:
        dict: status, delay, departure/arrival info
    """
    # Adjust the path as needed for your project structure
    # /app/data/sample_data.json
    sample_path = os.path.join(
        os.path.dirname(__file__),
        "../../data/sample_data.json"
    )
    try:
        with open(sample_path, "r") as f:
            data = json.load(f)

        flights = data.get("data", [])
        if not flights:
            return {"error": "No sample flights found."}

        # Optionally, filter by flight_number and flight_date if needed
        # For now, just use the first sample
        flight = flights[0]
        return {
            "airline": flight["airline"]["name"],
            "flight_number": flight["flight"]["iata"],
            "departure_airport": flight["departure"]["airport"],
            "arrival_airport": flight["arrival"]["airport"],
            "scheduled_departure": flight["departure"]["scheduled"],
            "status": flight["flight_status"],
            "delay_minutes": flight["departure"].get("delay", 0)
        }

    except Exception as e:
        return {"error": str(e)}
