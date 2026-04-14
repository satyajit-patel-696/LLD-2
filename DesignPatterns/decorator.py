from abc import ABC,abstractmethod
class Pizza(ABC):
    @abstractmethod
    def get_description(self)->str:
        pass
    @abstractmethod
    def get_cost(self)->float:pass
class PlainPizza(Pizza):
    def get_description(self) ->str:
        return "Plain Pizza"
    def get_cost(self)->float:
        return 5.0
class PizzaDecorator(Pizza):
    def __init__(self,pizza:Pizza):
        self.pizza=pizza
    def get_description(self)->str:
        return self.pizza.get_description()
    def get_cost(self) -> float:
        return self.pizza.get_cost()
class CheeseDecorator(PizzaDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description()+",milk"
    def get_cost(self) -> float:
        return self.pizza.get_cost()+3.0
class ChickenDecorator(PizzaDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description()+", cchicken"
    def get_cost(self) -> float:
        return self.pizza.get_cost()+9
p=PlainPizza()
print(p.get_description())
print(p.get_cost())
c=CheeseDecorator(ChickenDecorator(p))
print(c.get_description())
print(c.get_cost())