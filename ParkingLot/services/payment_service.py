import uuid
from datetime import datetime, timedelta

from dataclasses import dataclass

from ParkingLot.enums.payment_status import PaymentStatus
from ParkingLot.enums.payment_type import PaymentType
from ParkingLot.models.invoice import Invoice
from ParkingLot.models.payments import Payment
from ParkingLot.repositories.payment_repository import PaymentRepository
from ParkingLot.repositories.ticket_repository import TicketRepository
from ParkingLot.strategies.pricing_strategy import PricingStrategy
from ParkingLot.exceptions.parking_exceptions import PaymentNotFoundException, TicketNotFoundException, PaymentAlreadyDoneException
@dataclass
class PaymentService:
    payment_repository: PaymentRepository
    ticket_repository: TicketRepository
    pricing_strategy: PricingStrategy


    def process_payment(self, ticket_id: str, payment_type:PaymentType):
        ticket=self.ticket_repository.find_by_ticket_id(ticket_id)
        if not ticket:
            raise TicketNotFoundException(f"Ticket with id {ticket_id} not found")
        existing_payment=self.payment_repository.find_by_ticket_id(ticket_id)
        if existing_payment and existing_payment.payment_status==PaymentStatus.SUCCESS:
            raise PaymentAlreadyDoneException(f"Payment already done for ticket id {ticket_id}")
        current_time=datetime.now()
        amount=self.pricing_strategy.calculate_price(entry_time=ticket.entry_time,
                                                      exit_time=current_time,
                                                      spot_type=ticket.parking_spot.spot_type)
        payment_id=f"PAY-{uuid.uuid4().hex[:8]}"
        payment=Payment(payment_id=payment_id,
                        amount=amount,
                        payment_type=payment_type,
                        payment_status=PaymentStatus.SUCCESS,
                        payment_time=current_time,
                        ticket_id=ticket_id)
        self.payment_repository.save(payment)
        return payment
    def get_payment(self, ticket_id: str) -> Payment:
        """Get payment by ticket ID"""
        payment = self.payment_repository.find_by_ticket_id(ticket_id)
        if not payment:
            raise PaymentNotFoundException(f"Payment with id {ticket_id} not found")
        return payment
    def generate_invoice(self,ticket_id:str):
        ticket=self.ticket_repository.find_by_ticket_id(ticket_id)
        payment=self.get_payment(ticket_id)
        if not ticket:
            raise TicketNotFoundException(f"Ticket with id {ticket_id} not found")
        invoice_id=f"INV-{uuid.uuid4().hex[:8]}"
        invoice=Invoice(invoice_id=invoice_id,
                        ticket=ticket,
                        exit_time=datetime.now(), #for testing purpose, setting exit time 1 second after payment time
                        amount=payment.amount,
                        payment=payment)
        return invoice
    