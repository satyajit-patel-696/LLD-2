from dataclasses import dataclass

from ParkingLot.models.parking_ticket import ParkingTicket
from ParkingLot.models.payments import Payment
from ParkingLot.models.vehicle import Vehicle
from datetime import datetime

@dataclass
class Invoice:
    invoice_id: str
    ticket:ParkingTicket
    vehicle:Vehicle
    amount: float
    payment:Payment
    exit_time: datetime