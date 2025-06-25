import pytest
from unittest.mock import patch, MagicMock
from app.services.opensky_client import OpenSkyClient, AircraftState, OpenSkyResponse
from app.services.interfaces import IAirTrafficClient

@pytest.fixture
def mock_opensky_client():
    """Fixture to create a mock OpenSkyClient instance"""
    return OpenSkyClient()

@pytest.fixture
def mock_response_data():
    """Fixture for the mock response data"""
    return {
        "time": 1627314021,
        "states": [
            [
                "aa781f", "CKS616", "United States", 1750249263, 1750249263, -93.5969, 43.4371, 9753.6, False, 247.45, 313.48, 0, None, 10081.26, "4012", False, 0
            ],
            [
                "4b1900", "EDW16  ", "Switzerland", 1750249263, 1750249263, 3.8865, 48.2283, 10820.4, False, 242.11, 287.43, 3.25, None, 11391.9, "3052", False, 0
            ]
        ]
    }

def test_get_all_states(mock_opensky_client, mock_response_data):
    """Test the get_all_states method"""
    # Mock the HTTP response to return the mock_response_data
    with patch.object(mock_opensky_client.client, 'get', return_value=MagicMock(status_code=200, json=MagicMock(return_value=mock_response_data))) as mock_get:
        result = mock_opensky_client.get_all_states()

    assert result is not None
    assert isinstance(result, OpenSkyResponse)
    assert len(result.states) == 2
    assert result.states[0].icao24 == "aa781f"
    assert result.states[1].callsign == "EDW16"
    mock_get.assert_called_once()

def test_get_all_states_request_error(mock_opensky_client):
    """Test the get_all_states method handling request errors"""
    with patch.object(mock_opensky_client.client, 'get', side_effect=Exception("Request failed")):
        result = mock_opensky_client.get_all_states()

    assert result is None

def test_find_flight_by_callsign(mock_opensky_client, mock_response_data):
    """Test the find_flight_by_callsign method"""
    with patch.object(mock_opensky_client.client, 'get', return_value=MagicMock(status_code=200, json=MagicMock(return_value=mock_response_data))) as mock_get:
        result = mock_opensky_client.find_flight_by_callsign("CKS616")

    assert result is not None
    assert result.callsign == "CKS616"
    mock_get.assert_called_once()

def test_find_flight_by_callsign_not_found(mock_opensky_client, mock_response_data):
    """Test that the find_flight_by_callsign method returns None when flight is not found"""
    with patch.object(mock_opensky_client.client, 'get', return_value=MagicMock(status_code=200, json=MagicMock(return_value=mock_response_data))) as mock_get:
        result = mock_opensky_client.find_flight_by_callsign("UNKNOWN123")

    assert result is None
    mock_get.assert_called_once()

def test_parse_state_error_handling(mock_opensky_client, mock_response_data):
    """Test that the _parse_state method gracefully handles incomplete or malformed data"""
    incomplete_data = mock_response_data["states"] + [
        ["icao24_3", "TEST123"]  # Incomplete data (missing fields)
    ]

    with patch.object(mock_opensky_client.client, 'get', return_value=MagicMock(status_code=200, json=MagicMock(return_value={"time": 1627314021, "states": incomplete_data}))) as mock_get:
        result = mock_opensky_client.get_all_states()

    # Ensure that the method doesn't crash on incomplete data
    assert result is not None
    assert len(result.states) == 2
    mock_get.assert_called_once()
