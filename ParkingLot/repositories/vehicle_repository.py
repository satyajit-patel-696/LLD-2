from dataclasses import dataclass, field
from ..models.vehicle import Vehicle
from ..enums.vehicle_type import VehicleType
from typing import Optional
@dataclass
class VehicleRepository:
    vehicles:dict[str,Vehicle]=field(default_factory=dict)
    
    def save(self, vehicle:Vehicle): #license_plate to vehicle mapping
        self.vehicles[vehicle.license_plate] = vehicle
    def find_by_license_plate(self, license_plate:str)->Optional[Vehicle]:
        return self.vehicles.get(license_plate)