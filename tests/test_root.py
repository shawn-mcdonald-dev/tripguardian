def test_root_endpoint_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "TripGuardian is running!"
