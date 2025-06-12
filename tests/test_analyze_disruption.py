import copy

class TestAnalyzeDisruption:

    def test_valid_input_returns_200(self, client, valid_request_data):
        response = client.post("/analyze_disruption", json=valid_request_data)
        assert response.status_code == 200
        data = response.json()
        assert "trip_id" in data
        assert "disruption_level" in data
        assert "suggested_action" in data
    
    def test_disruption_low_returns_1(self, client, valid_request_data):
        data = copy.deepcopy(valid_request_data)
        data["flights"][0]["delay_mins"] = 10  # Low delay
        response = client.post("/disruption_check", json=data)
        assert response.status_code == 200
        assert response.json()["disruption_level"] == 1
        
    '''
    def test_missing_trip_id_returns_422(self, client, valid_request_data):
        data = copy.deepcopy(valid_request_data)
        data["trip_id"] = ""
        response = client.post("/analyze_disruption", json=data)
        assert response.status_code == 422

    def test_negative_delay_returns_422(self, client, valid_request_data):
        data = copy.deepcopy(valid_request_data)
        data["flights"][0]["delay_mins"] = -10
        response = client.post("/analyze_disruption", json=data)
        assert response.status_code == 422

    def test_empty_weather_returns_422(self, client, valid_request_data):
        data = copy.deepcopy(valid_request_data)
        data["weather"] = {}
        response = client.post("/analyze_disruption", json=data)
        assert response.status_code == 422
    '''