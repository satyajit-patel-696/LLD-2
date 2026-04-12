from dataclasses import dataclass
from typing import Optional

from ParkingLot.enums.spot_status import SpotStatus
from ParkingLot.models.parking_spot import ParkingSpot

@dataclass
class ParkingSpotRepository:
    parking_spots: dict[str, ParkingSpot] = {}   #spot_id to parking spot mapping

    def save(self, spot:ParkingSpot):
        self.parking_spots[spot.spot_id] = spot
    def find_by_spot_id(self, spot_id:str)->Optional[ParkingSpot]:
        return self.parking_spots.get(spot_id)
    def find_all(self)->list[ParkingSpot]:
        return list(self.parking_spots.values())
    def find_available_by_type(self, spot_type:str)->list[ParkingSpot]:
        return [s for s in self.parking_spots.values() if s.spot_type==spot_type and s.is_avilable()]
    def find_avilable_spots(self)->list[ParkingSpot]:
        return [s for s in self.parking_spots.values() if s.is_avilable()]
    def update_status(self, spot_id:str, status:SpotStatus)->Optional[ParkingSpot]:
        spot = self.find_by_spot_id(spot_id)
        if spot:
            spot.spot_status = status
        return spot