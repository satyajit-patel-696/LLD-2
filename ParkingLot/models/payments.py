from dataclasses import dataclass
from datetime import datetime

from ParkingLot.enums.payment_status import PaymentStatus
from ParkingLot.enums.payment_type import PaymentType

@dataclass
class Payment:
    payment_id: str
    amount: float
    payment_type:PaymentType
    payment_status:PaymentStatus
    payment_time: datetime
    ticket_id: str
