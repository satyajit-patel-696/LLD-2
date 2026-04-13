


from abc import ABC, abstractmethod
from datetime import datetime

from ParkingLot.enums.spot_type import SpotType



class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self,entry_time: datetime, exit_time: datetime,spot_type: SpotType) -> float:
        pass

class HourlyPricingStrategy(PricingStrategy):
    SPOT_TYPE_RATE = {
        SpotType.SMALL: 10.0,
        SpotType.MEDIUM: 20.0,
        SpotType.LARGE: 30.0,
    }
    def calculate_price(self, entry_time: datetime, exit_time: datetime, spot_type: SpotType) -> float:
        duration = (exit_time - entry_time).total_seconds() / 3600
        rate = self.SPOT_TYPE_RATE.get(spot_type,0)
        return duration * rate