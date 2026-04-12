from dataclasses import dataclass

from ParkingLot.models.parking_floor import ParkingFloor
from ParkingLot.models.parking_gate import ParkingGate

@dataclass
class ParkingSlot:
    id:str
    name:str
    address:str
    floors:list[ParkingFloor]
    entry_gates:list[ParkingGate]
    exit_gates:list[ParkingGate]
    def add_floor(self,floor:ParkingFloor):
        self.floors.append(floor)
    def add_entry_gate(self,gate:ParkingGate):
        self.entry_gates.append(gate)
    def add_exit_gate(self,gate:ParkingGate):   
        self.exit_gates.append(gate)