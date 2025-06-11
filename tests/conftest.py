import pytest
from fastapi.testclient import TestClient
from app.main import app

# --- Fixtures ---

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_request_data():
    return {
        "trip_id": "abc123",
        "flights": [
            {"from_": "JFK", "to": "LHR", "delay_mins": 45},
            {"from_": "LHR", "to": "BER", "delay_mins": 90}
        ],
        "weather": {
            "LHR": "Fog",
            "BER": "Clear"
        },
        "current_location": "LHR"
    }