from dataclasses import dataclass
from datetime import datetime
import uuid

from ParkingLot.enums.vehicle_type import VehicleType
from ParkingLot.exceptions.parking_exceptions import TicketNotFoundException
from ParkingLot.models.parking_ticket import ParkingTicket
from ParkingLot.models.parking_ticket import ParkingTicket
from ParkingLot.repositories.parking_spot_repository import ParkingSpotRepository
from ParkingLot.repositories.ticket_repository import TicketRepository
from ParkingLot.repositories.vehicle_repository import VehicleRepository
from ParkingLot.strategies.pricing_strategy import PricingStrategy
from ParkingLot.models.parking_attendant import ParkingAttendant
from ParkingLot.models.parking_gate import ParkingGate
from typing import Optional
from ParkingLot.models.vehicle import Vehicle
from ParkingLot.strategies.spot_allocation_strategy import SpotAllocationStrategy


@dataclass
class TicketService:
    allocation_strategy:SpotAllocationStrategy
    spot_repository:ParkingSpotRepository
    vehicle_repository:VehicleRepository
    ticket_repository:TicketRepository

    def issue_ticket(self, vehicle_license_plate:str,
                     vehicle_type:VehicleType,
                       entry_gate_id:ParkingGate,
                    entry_time:datetime,
                         entry_attendant:Optional[ParkingAttendant]=None):
        vehicle=self.vehicle_repository.find_by_license_plate(vehicle_license_plate)
        if not vehicle:
            vehicle=Vehicle(license_plate=vehicle_license_plate, vehicle_type=vehicle_type)
            self.vehicle_repository.save(vehicle)
        avilable_spot=self.spot_repository.find_avilable_spots()
        spot=self.allocation_strategy.find_spot(vehicle_type=vehicle_type,avilable_spots=avilable_spot)
        if not spot:
            raise Exception("No avilable spot for this vehicle type")
        spot.occupy()
        self.spot_repository.save(spot)
        ticket_id=f"TKT-{uuid.uuid4().hex[:8]}"
        ticket=ParkingTicket(ticket_id=ticket_id, 
                           vehicle=vehicle, 
                           parking_spot=spot, 
                           entry_gate=entry_gate_id,
                         entry_time=entry_time, #for testing purpose, setting entry time 2 hours back    
                           entry_attendant=entry_attendant)
        self.ticket_repository.save(ticket)
        return ticket
    def get_ticket(self, ticket_id: str) -> ParkingTicket:
        """Get ticket by ID"""
        ticket = self.ticket_repository.find_by_ticket_id(ticket_id)
        if not ticket:
            raise TicketNotFoundException(ticket_id)
        return ticket

    def free_spot(self, ticket_id: str):
        """Free the parking spot associated with a ticket"""
        ticket = self.get_ticket(ticket_id)
        ticket.parking_spot.free()
        self.spot_repository.save(ticket.parking_spot)
    

        

    