from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas import DisruptionRequest
from app.logic import get_disruption_level, suggest_action
from app.services.flight_status import get_flight_status, get_sample_flight_status
from app.services.flight_search import get_alternative_flights

app = FastAPI(
    title="TripGuardian API",
    description="API that detects real-time disruptions and proactively recommends actions to travelers.",
    version="1.0.0"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body},
    )

@app.get("/status")
def flight_status(flight_number: str = Query(..., example="AA100"),
                  flight_date: str = Query(..., example="2025-06-13")):
    """
    Check the real-time status of a flight.
    """
    # result = get_flight_status(flight_number, flight_date)
    result = get_flight_status(flight_number, flight_date)
    return result

@app.get("/rebook")
def rebook_options(flight_number: str = Query(..., example="AA100"),
                   flight_date: str = Query(..., example="2025-06-17")):
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

@app.get("/")
def root():
    return {"message": "TripGuardian is running!"}

@app.post(
    "/analyze_disruption",
    response_model=dict,
    summary="Analyze travel disruptions",
    response_description="Analysis of the submitted disruption data"
)
def analyze_disruption(data: DisruptionRequest):
    """
    Analyze a travel disruption based on submitted itinerary, delays, and weather.

    - **trip_id**: Unique trip identifier
    - **flights**: List of flight legs (from, to, delay_mins)
    - **weather**: Mapping of airport code to weather condition
    - **current_location**: Current airport code
    """
    return {
        "trip_id": data.trip_id,
        "status": "received",
        "disruption_level": "TBD",
        "suggested_action": "TBD"
    }

@app.post("/disruption_check")
def assess_disruption(data: DisruptionRequest):
    level = get_disruption_level(data.flights[0].delay_mins)
    action = suggest_action(level)
    return {
        "disruption_level": level,
        "suggested_action": action,
    }