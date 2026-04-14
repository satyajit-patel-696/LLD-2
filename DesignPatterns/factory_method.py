from abc import ABC,abstractmethod
class Vechile(ABC):
    @abstractmethod
    def drive(self):
        pass
class Car(Vechile):
    def drive(self):
        print("driving car")
class Bike(Vechile):
    def drive(self):
        print("riding bike")
class VechileFactory(ABC):
    @abstractmethod
    def create_vechile(self)->Vechile:
        pass
    def deliver(self):
        vechile=self.create_vechile()
        vechile.drive()
class CarFactory(VechileFactory):
    def create_vechile(self) -> Vechile:
        return Car()
class BikeFactory(VechileFactory):
    def create_vechile(self) -> Vechile:
        return Bike()
if __name__=="__main__":
    car=CarFactory()
    car.deliver()