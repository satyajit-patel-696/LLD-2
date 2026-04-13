


from datetime import datetime,timedelta

from ParkingLot.enums.spot_type import SpotType
from ParkingLot.enums.spot_status import SpotStatus
from ParkingLot.enums.vehicle_type import VehicleType
from ParkingLot.enums.payment_type import PaymentType
from ParkingLot.enums.gate_type import GateType
from ParkingLot.models.parking_attendant import ParkingAttendant
from ParkingLot.models.parking_gate import ParkingGate
from ParkingLot.controllers.ticket_controller import TicketController
from ParkingLot.controllers.payment_controller import PaymentController
from ParkingLot.repositories.parking_spot_repository import ParkingSpotRepository
from ParkingLot.models.parking_spot import ParkingSpot
from ParkingLot.repositories.payment_repository import PaymentRepository
from ParkingLot.repositories.ticket_repository import TicketRepository
from ParkingLot.repositories.vehicle_repository import VehicleRepository
from ParkingLot.strategies.nearest_spot_strategy import NearestSpotStrategy
from ParkingLot.strategies.pricing_strategy import HourlyPricingStrategy
from ParkingLot.services.ticket_service import TicketService
from ParkingLot.services.payment_service import PaymentService

def setup_parking_lot():
    spot_repository=ParkingSpotRepository()
    spots=[ParkingSpot(f"SPT-1", 1, SpotType.SMALL, SpotStatus.FREE, "F1"),
           ParkingSpot(f"SPT-2", 2, SpotType.SMALL, SpotStatus.FREE, "F1"),
           ParkingSpot(f"SPT-3", 3, SpotType.MEDIUM, SpotStatus.FREE, "F1"),
           ParkingSpot(f"SPT-4", 4, SpotType.MEDIUM, SpotStatus.FREE, "F1"),
           ParkingSpot(f"SPT-5", 5, SpotType.LARGE, SpotStatus.FREE, "F1"),]
    for spot in spots:
        spot_repository.save(spot)
    return spot_repository
def main():
    #running the parking lot system
    print("="*60)
    print("Welcome to the Parking Lot System")
    print("="*60)
    spot_repository=setup_parking_lot()
    vehicle_repository=VehicleRepository()
    ticket_repository=TicketRepository()
    payment_repository=PaymentRepository()
    allocation_strategy=NearestSpotStrategy()
    pricing_strategy=HourlyPricingStrategy()

    ticket_service = TicketService(
        allocation_strategy=allocation_strategy,
        spot_repository=spot_repository,
        vehicle_repository=vehicle_repository,
        ticket_repository=ticket_repository,
    )
    payment_service = PaymentService(
        payment_repository=payment_repository,
        ticket_repository=ticket_repository,
        pricing_strategy=pricing_strategy,
    )

    ticket_controller = TicketController(ticket_service=ticket_service)
    payment_controller = PaymentController(payment_service=payment_service)

    entry_attendant = ParkingAttendant(
        id="ATT-1",
        name="John",
        email="john@parkinglot.com",
    )
    entry_gate = ParkingGate(
        gate_id=1,
        gate_type=GateType.ENTRY,
        attendant=entry_attendant,
    )

    ticket = ticket_controller.issue_ticket(
        vehicle_license_plate="KA01AB1234",
        vehicle_type=VehicleType.CAR,
        entry_gate_id=entry_gate,
        entry_time=datetime.now()-timedelta(hours=6), # for testing purpose, set entry time 9 hours back
        entry_attendant=entry_attendant,
    )
    print(f"Ticket issued: {ticket.ticket_id}, Spot: {ticket.parking_spot.spot_number}")

    fetched_ticket = ticket_controller.get_ticket(ticket.ticket_id)
    print(f"Fetched ticket for vehicle: {fetched_ticket.vehicle.license_plate}")

    payment = payment_controller.process_payment(
        ticket_id=ticket.ticket_id,
        payment_type=PaymentType.CARD,
    )
    print(f"Payment successful: {payment.payment_id}, Amount: {payment.amount:.2f}")

    invoice = payment_controller.generate_invoice(ticket.ticket_id)
    print(f"Invoice generated: {invoice.invoice_id}, Final amount: {invoice.amount:.2f}")


if __name__ == "__main__":
    main()
    