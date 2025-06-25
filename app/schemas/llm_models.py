from pydantic import BaseModel

class RerouteRequest(BaseModel):
    origin: str
    destination: str
    delay_minutes: int
    weather_conditions: str
    user_priority: str
  
class RerouteResponse(BaseModel):
    suggestion: str