from fastapi import FastAPI, HTTPException
from app.schemas import DisruptionRequest

app = FastAPI()

@app.get("/")
def root():
    return {"message": "TripGuardian is running!"}

@app.post("/analyze_disruption")
def analyze_disruption(data: DisruptionRequest):
    # Placeholder response
    return {
        "trip_id": data.trip_id,
        "status": "received",
        "disruption_level": "TBD",
        "suggested_action": "TBD"
    }
