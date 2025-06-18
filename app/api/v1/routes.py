from fastapi import APIRouter, HTTPException, Query, Depends
from app.services.flight_status import get_flight_status
from app.services.flight_search import get_alternative_flights
from app.services.opensky_client import OpenSkyClient
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def get_opensky_client() -> OpenSkyClient:
    return OpenSkyClient()

@router.get("/status")
def flight_status(
    flight_number: str = Query(..., examples="e.g. AA100"),
    client: OpenSkyClient = Depends(get_opensky_client)
):
    """
    Check the real-time status of a flight.
    """
    flight = client.find_flight_by_callsign(flight_number)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    return flight.model_dump()

'''
@router.get("/rebook")
def rebook_options(flight_number: str = Query(..., examples="AA100"),
                   flight_date: str = Query(..., examples="2025-06-17")):
    """
    Combines flight status check with rebooking alternatives (if delayed or cancelled).
    """
    status = get_flight_status(flight_number, flight_date)

    if "error" in status:
        return {"status": status, "alternatives": []}

    # Check if the flight is on time
    if status["status"] not in ["cancelled", "incident", "diverted"]:
        return {
            "status": status,
            "message": "Your flight is on time. No rebooking options necessary.",
            "alternatives": []
        }

    # Use flight info for rebooking
    origin = status["departure_airport"]
    destination = status["arrival_airport"]
    after_time = status["scheduled_departure"]  # ISO format

    alt_flights = get_alternative_flights(origin, destination, after_time)

    return {
        "status": status,
        "message": "Your flight is disrupted. Here are rebooking options.",
        "alternatives": alt_flights
    }
'''
