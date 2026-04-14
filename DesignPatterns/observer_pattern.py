from abc import ABC,abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self,weather):pass
class PhoneDisplay(Observer):
    def __init__(self):
        self.weather=""
    def update(self,weather:str):
        self.weather=weather
        self.display()
    def display(self):
        print(f"current weather is {self.weather}")
class TvDisplay(Observer):
    def __init__(self):
        self.weather=""
    def update(self,weather:str):
        self.weather=weather
        self.display()
    def display(self):
        print("tv diplay the updated weathger is {self.weather}")
class Subject(ABC):
    @abstractmethod
    def add_observer(self,observer:Observer):pass
    @abstractmethod
    def remove_observer(self,observer:Observer):pass
class WeatherStation(Subject):
    def __init__(self):
        self.observers:list[Observer]=[]
        self.weather=""
    def add_observer(self, observer: Observer):
        self.observers.append(observer)
    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
    def notify_observers(self):
        for o in self.observers:
            o.update(self.weather)
    def set_weather(self,new_weather:str):
        self.weather=new_weather
        self.notify_observers()
phone=PhoneDisplay()
tv=TvDisplay()
wstation=WeatherStation()
wstation.add_observer(phone)
wstation.add_observer(tv)
wstation.set_weather("sunny")
