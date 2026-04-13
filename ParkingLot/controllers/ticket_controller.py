

from dataclasses import dataclass
from datetime import datetime

from ParkingLot.enums.vehicle_type import VehicleType
from ParkingLot.models.parking_attendant import ParkingAttendant
from ParkingLot.models.parking_gate import ParkingGate
from ParkingLot.services.ticket_service import TicketService


@dataclass
class TicketController:
    ticket_service: TicketService
    def issue_ticket(self, vehicle_license_plate:str,vehicle_type:VehicleType, entry_gate_id:ParkingGate,
                      entry_time:datetime,entry_attendant:ParkingAttendant):
        return self.ticket_service.issue_ticket(vehicle_license_plate=vehicle_license_plate,
                                                vehicle_type=vehicle_type,
                                                entry_gate_id=entry_gate_id,
                                                entry_time=entry_time,
                                                entry_attendant=entry_attendant)
    def get_ticket(self, ticket_id: str):
        return self.ticket_service.get_ticket(ticket_id)