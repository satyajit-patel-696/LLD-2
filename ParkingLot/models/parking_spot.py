from dataclasses import dataclass
from typing import Optional
from ParkingLot.enums.spot_type import SpotType
from ParkingLot.enums.spot_status import SpotStatus

@dataclass
class ParkingSpot:    
    spot_id: str
    spot_number: int
    spot_type:SpotType
    spot_status:SpotStatus=SpotStatus.FREE
    floor_id: str = ""

    def is_available(self):
        return self.spot_status == SpotStatus.FREE

    def is_avilable(self):
        # Backward-compatible alias used by existing repository/strategy code.
        return self.is_available()

    def occupy(self):
        self.spot_status=SpotStatus.OCCUPIED
    def free(self):
        self.spot_status=SpotStatus.FREE
    