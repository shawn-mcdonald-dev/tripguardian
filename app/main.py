from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas import DisruptionRequest
from app.logic import get_disruption_level, suggest_action

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
    level = get_disruption_level(data.delay_mins)
    action = suggest_action(level)
    return {
        "disruption_level": level,
        "suggested_action": action,
    }