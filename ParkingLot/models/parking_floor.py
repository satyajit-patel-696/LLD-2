from dataclasses import dataclass

from .parking_spot import  ParkingSpot
@dataclass
class ParkingFloor:
    id:str
    floor_number:int
    spots:list[ParkingSpot]

    def add_spot(self,slot:ParkingSpot):
        self.spots.append(slot)
    def get_avilable_spots(self):
        return [s for s in self.spots if s.is_avilable()]
    
