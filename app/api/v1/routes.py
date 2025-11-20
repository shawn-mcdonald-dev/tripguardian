from fastapi import APIRouter, HTTPException, Query, Depends
from app.services.flight_status import get_flight_status
from app.services.flight_search import get_alternative_flights
from app.langchain.chains.reroute_chain import suggest_reroute
from app.langchain.config import get_llm
from app.schemas.llm_models import RerouteRequest, RerouteResponse
from langchain.chat_models.base import BaseChatModel
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/reroute", response_model=RerouteResponse)
def reroute_advice(
    request: RerouteRequest,
    llm: BaseChatModel = Depends(get_llm)
):
    try:
        suggestion = suggest_reroute(request.model_dump(), llm=llm)
        return {"suggestion": suggestion}
    except Exception as e:
        logger.exception("Error in reroute_advice")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/rebook")
def rebook_options(flight_number: str = Query(..., examples=["AA100"]),
                   flight_date: str = Query(..., examples=["2025-06-17"])):
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
