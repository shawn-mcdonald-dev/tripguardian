from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint_returns_200():
    response = client.get("/")
    assert response.status_code == 200, "Expected 200 OK from root endpoint"
    
    data = response.json()
    assert isinstance(data, dict), "Response should be a JSON object"
    assert "message" in data, "Response should include a 'message' key"
    assert data["message"] == "TripGuardian is running!", "Unexpected root message content"