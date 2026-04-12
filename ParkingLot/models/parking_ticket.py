from dataclasses import dataclass
from typing import Optional
from ParkingLot.models.parking_attendant import ParkingAttendant
from datetime import datetime
from ParkingLot.models.parking_gate import ParkingGate
from ParkingLot.models.parking_spot import ParkingSpot
from .vehicle import Vehicle
@dataclass
class ParkingTicket:
    ticket_id:str
    vehicle:Vehicle
    entry_gate:ParkingGate
    entry_time:datetime
    parking_spot:ParkingSpot
    entry_attendant:Optional[ParkingAttendant] = None
    