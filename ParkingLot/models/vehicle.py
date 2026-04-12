from dataclasses import dataclass
from ..enums.vehicle_type import VechileType
@dataclass
class Vehicle:
    license_plate:str
    vehicle_type:str

    def _post_init__(self):
        if  not isinstance(self.vehicle_type,VechileType):
            raise ValueError(f"Invalid vehicle type {self.vehicle_type}")