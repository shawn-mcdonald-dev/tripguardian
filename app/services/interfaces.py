from abc import ABC, abstractmethod
from typing import Optional
from app.schemas.models import OpenSkyResponse, AircraftState

class IAirTrafficClient(ABC):
    """
    Interface for an air traffic client that can fetch aircraft state data.
    Implementations of this interface should provide methods to retrieve all aircraft states
    and to find a specific flight by its callsign.
    """

    @abstractmethod
    def get_all_states(self) -> Optional[OpenSkyResponse]:
        """
        Retrieve the current state vectors for all aircraft.
        Returns:
            Optional[OpenSkyResponse]: An OpenSkyResponse object containing all aircraft states,
            or None if the data could not be retrieved.
        """
        pass

    @abstractmethod
    def find_flight_by_callsign(self, callsign: str) -> Optional[AircraftState]:
        """
        Find and return the state of a specific flight by its callsign.
        Args:
            callsign (str): The callsign of the flight to search for.
        Returns:
            Optional[AircraftState]: The state of the aircraft with the given callsign,
            or None if not found.
        """
        pass
