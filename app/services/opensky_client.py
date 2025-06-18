import logging
from typing import Optional, List
import httpx
from app.schemas.models import AircraftState, OpenSkyResponse
from app.services.interfaces import IAirTrafficClient

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class OpenSkyClient(IAirTrafficClient):
    BASE_URL = "https://opensky-network.org/api"

    def __init__(self, username: Optional[str] = None, password: Optional[str] = None, client: Optional[httpx.Client] = None):
        self.auth = (username, password) if username and password else None
        self.client = client or httpx.Client(timeout=10)

    def get_all_states(self) -> Optional[OpenSkyResponse]:
        url = f"{self.BASE_URL}/states/all"
        try:
            logger.info("Fetching real-time aircraft states from OpenSky")
            response = self.client.get(url, auth=self.auth)
            response.raise_for_status()
            data = response.json()

            states = [self._parse_state(s) for s in data.get("states", [])]
            states = [s for s in states if s is not None]

            return OpenSkyResponse(
                time=data["time"],
                states=states
            )

        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
        except Exception as e:
            logger.exception("Unexpected error occurred")

        return None

    def find_flight_by_callsign(self, callsign: str) -> Optional[AircraftState]:
        data = self.get_all_states()
        if not data:
            return None

        normalized = callsign.strip().upper()
        return next((s for s in data.states if s.callsign and normalized in s.callsign.upper()), None)

    def _parse_state(self, s: List) -> AircraftState:
        if len(s) < 17:
            logger.warning(f"Incomplete state data: {s}")
            return None

        return AircraftState(
            icao24=s[0],
            callsign=s[1].strip() if s[1] else None,
            origin_country=s[2],
            time_position=s[3],
            last_contact=s[4],
            longitude=s[5],
            latitude=s[6],
            baro_altitude=s[7],
            on_ground=s[8],
            velocity=s[9],
            true_track=s[10],
            vertical_rate=s[11],
            sensors=s[12],
            geo_altitude=s[13],
            squawk=s[14],
            spi=s[15],
            position_source=s[16]
        )

