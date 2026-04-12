from .spot_allocation_strategy import SpotAllocationStrategy
from ParkingLot.enums.vehicle_type import VehicleType
from ParkingLot.models.parking_spot import ParkingSpot
from typing import Optional
class NearestSpotStrategy(SpotAllocationStrategy):
    VEHICLE_TO_SPOT_MAPPING = {
        VehicleType.BIKE: SpotType.SMALL,
        VehicleType.SCOOTER: SpotType.SMALL,
        VehicleType.CAR: SpotType.MEDIUM,
        VehicleType.TRUCK: SpotType.LARGE,
        VehicleType.BUS: SpotType.LARGE,
    }
    def find_spot(self, vehicle_type: VehicleType, avilable_spots: list[ParkingSpot])->Optional[ParkingSpot]: -> Optional[ParkingSpot]:
        for spot in avilable_spots:
            if spot.is_avilable() and spot.spot_type.value == vehicle_type.value: