from dataclasses import dataclass

from ParkingLot.enums.payment_type import PaymentType
from ParkingLot.services.payment_service import PaymentService

@dataclass
class PaymentController:
    payment_service: PaymentService

    def process_payment(self, ticket_id: str, payment_type:PaymentType):
        return self.payment_service.process_payment(ticket_id, payment_type)

    def get_payment(self, ticket_id: str):
        return self.payment_service.get_payment(ticket_id)

    def generate_invoice(self,ticket_id:str):
        return self.payment_service.generate_invoice(ticket_id)