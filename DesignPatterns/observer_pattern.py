from abc import ABC,abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self,weather) -> None:pass
class PhoneDisplay(Observer):
    def __init__(self) -> None:
        self.weather: str=""
    def update(self,weather:str) -> None:
        self.weather: str=weather
        self.display()
    def display(self) -> None:
        print(f"current weather is {self.weather}")
class TvDisplay(Observer):
    def __init__(self) -> None:
        self.weather: str=""
    def update(self,weather:str) -> None:
        self.weather: str=weather
        self.display()
    def display(self) -> None:
        print("tv diplay the updated weathger is {self.weather}")
class Subject(ABC):
    @abstractmethod
    def add_observer(self,observer:Observer) -> None:pass
    @abstractmethod
    def remove_observer(self,observer:Observer) -> None:pass
class WeatherStation(Subject):
    def __init__(self) -> None:
        self.observers:list[Observer]=[]
        self.weather: str=""
    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)
    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)
    def notify_observers(self) -> None:
        for o in self.observers:
            o.update(self.weather)
    def set_weather(self,new_weather:str) -> None:
        self.weather: str=new_weather
        self.notify_observers()
phone=PhoneDisplay()
tv=TvDisplay()
wstation=WeatherStation()
wstation.add_observer(phone)
wstation.add_observer(tv)
wstation.set_weather("sunny")
