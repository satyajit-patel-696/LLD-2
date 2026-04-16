class Discount:
    def discount_strategy(self,customer_type:str):
        if customer_type=="Gold":
            return 0.5
        if customer_type=="Silver":
            return 0.1
from abc import ABC,abstractmethod
class DiscountL(ABC):
    @abstractmethod
    def get_discount(self):
        pass
class PremiumCusotmer(DiscountL):
    def get_discount(self):
        return 10
class GoldCustomer(DiscountL):
    def get_discount(self):
        return 5
class Client:
    def __init__(self,d:DiscountL):
        self.d=d
    def calculate(self):
        return self.d.get_discount()
c=Client(GoldCustomer())
print(c.calculate())