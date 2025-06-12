from pydantic import BaseModel
from typing import List, Dict

class DisruptionRequest(BaseModel):
    trip_id: str
    from_: str
    to: str
    delay_mins: int
    weather: Dict[str, str]
    current_location: str
