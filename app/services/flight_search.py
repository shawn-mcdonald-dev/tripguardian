import os
import requests
from datetime import datetime, timedelta

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "kiwi-com-cheap-flights.p.rapidapi.com"
BASE_URL = "https://kiwi-com-cheap-flights.p.rapidapi.com/one-way"
# https://kiwi-com-cheap-flights.p.rapidapi.com/round-trip


def get_alternative_flights(departure_iata: str, arrival_iata: str, after_time: str, max_results: int = 5) -> list:
    """
    Search for alternative flights using the Kiwi.com API on RapidAPI.

    Parameters:
        departure_iata (str): IATA code (e.g., 'JFK')
        arrival_iata (str): IATA code (e.g., 'LAX')
        after_time (str): ISO datetime string (e.g., '2025-06-13T15:30:00Z')
        max_results (int): Number of top options to return

    Returns:
        list: A list of flight options sorted by price
    """
    try:
        dt_obj = datetime.fromisoformat(after_time.replace("Z", "+00:00"))
        date_from = dt_obj.strftime("%d/%m/%Y")
        time_from = dt_obj.strftime("%H:%M")

        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": RAPIDAPI_HOST
        }

        params = {
            "source": departure_iata,
            "destination": arrival_iata,
            "currency": "usd",
            "locale": "en",
            "adults": "1",
            "cabin_class": "economy",
            "sort_by": "PRICE",
            "limit": max_results,

            "date_from": date_from,
            "date_to": date_from,
            "time_from": time_from,
            "sort": "price"
        }

        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        flights = data.get("data", [])
        if not flights:
            return [{"note": "No rebooking options found."}]

        results = []
        for flight in flights:
            results.append({
                "airline": flight["airlines"][0],
                "flight_duration": flight["fly_duration"],
                "departure": flight["dTimeUTC"],
                "arrival": flight["aTimeUTC"],
                "price_usd": flight["price"],
                "booking_link": flight["deep_link"]
            })

        return results

    except Exception as e:
        return [{"error": str(e)}]
