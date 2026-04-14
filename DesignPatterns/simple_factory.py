from abc import ABC, abstractmethod
class Vechile(ABC):
    @abstractmethod
    def drive(self):
        pass
class Car(Vechile):
    def drive(self):
        print("driving a car")
class Bike(Vechile):
    def drive(self):
        print("driving a bike")
class VechileFactory:
    @staticmethod
    def create_vechile(vechile_type:str)->Vechile:
        if vechile_type=="car":
            return Car()
        elif vechile_type=="bike":
            return Bike()
        else:
            raise ValueError("invalid vechile type")
if __name__=="__main__":
    car=VechileFactory.create_vechile("car")
    bike=VechileFactory.create_vechile("bike")
    car.drive()
    bike.drive()