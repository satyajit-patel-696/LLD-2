import copy

class Engine:
    def __init__(self,power:int):
        self.power=power
class Car:
    def __init__(self,brand:str,engine:Engine):
        self.brand=brand
        self.engine=engine
    def clone(self)->"Car":
        return copy.deepcopy(self)
    def __repr__(self):
        return f"print {self.brand} is {self.engine}"
engine=Engine(9000)
car=Car("tata",engine)
car2=car.clone()
car2.brand="hyundai"

print(car.brand)
print(car2.brand)

    
