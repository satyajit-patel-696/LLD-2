

from ParkingLot.enums.vehicle_type import VehicleType
from ParkingLot.models.parking_spot import ParkingSpot
from typing import Optional

class SpotAllocationStrategy:
    def find_spot(self,vehicle_type:VehicleType,avilable_spots:list[ParkingSpot])->Optional[ParkingSpot]:
        pass
