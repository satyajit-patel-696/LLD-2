from dataclasses import dataclass
from typing import Optional
from ..models.parking_ticket import ParkingTicket
@dataclass
class TicketRepository:
    tickets: dict[str,ParkingTicket] = {}   #ticket_id to parking ticket mapping

    def save(self, ticket:ParkingTicket):
        self.tickets[ticket.ticket_id] = ticket
    def find_by_ticket_id(self, ticket_id:str)->Optional[ParkingTicket]:
        return self.tickets.get(ticket_id)
    def find_all(self)->list[ParkingTicket]:
        return list(self.tickets.values())