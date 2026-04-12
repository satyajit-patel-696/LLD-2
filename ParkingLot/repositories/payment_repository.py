from dataclasses import dataclass
from typing import Optional

from ParkingLot.models.payments import Payment

@dataclass
class PaymentRepository:
    payments: dict[str, Payment] = {}   #payment_id to payment mapping  
    ticket_id_to_payment: dict[str, Payment] = {}  #ticket_id to payment mapping
    def save(self, payment:Payment):
        self.payments[payment.payment_id] = payment
        self.ticket_id_to_payment[payment.ticket_id] = payment
    def find_by_payment_id(self, payment_id:str)->Optional[Payment]:
        return self.payments.get(payment_id)
    def find_by_ticket_id(self, ticket_id:str)->Optional[Payment]:
        return self.ticket_id_to_payment.get(ticket_id)
