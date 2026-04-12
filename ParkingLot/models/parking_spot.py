from dataclasses import dataclass
from enums.spot_type import SpotType
from enums.spot_status import SpotStatus

@dataclass
class ParkingSpot:    
    spot_id: str
    slot_number: int
    spot_type:SpotType
    spot_status:SpotStatus
    floor_number: int

    def is_avilable(self):
        return self .spot_status==SpotStatus.FREE
    def occupy(self):
        self.slot_status=SpotStatus.OCCUPIED
    def free(self):
        self.slot_status=SpotStatus.FREE
    