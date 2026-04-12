from dataclasses import dataclass

from typing import Optional
from ..enums.gate_type import GateType
from .parking_attendant import ParkingAttendant
@dataclass
class ParkingGate:
    gate_id:int
    gate_type:GateType
    attendant: Optional[ParkingAttendant] = None
    