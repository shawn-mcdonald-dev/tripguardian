from pydantic import BaseModel, field_validator
from typing import List, Dict

class FlightLeg(BaseModel):
    from_: str
    to: str
    delay_mins: int

class DisruptionRequest(BaseModel):
    trip_id: str
    flights: List[FlightLeg]
    weather: Dict[str, str]
    current_location: str
