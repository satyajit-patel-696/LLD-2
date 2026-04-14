from abc import ABC,abstractmethod
class Button(ABC):
    @abstractmethod
    def render(self):pass
class Menu(ABC):
    @abstractmethod
    def show(self):pass
class AndroidButton(Button):
    def render(self):
        print("rendering android button")
class AndroidMenu(Menu):
    def show(self):
        print("sjoeing android menu")
class IosButton(Button):
    def render(self):
        print("showing ios button")
class IosMenu(Menu):
    def show(self):
        print("showing ios menu")

class UiFactory(ABC):
    @abstractmethod
    def create_button(self)->Button:pass
    @abstractmethod
    def create_menu(self)->Menu:pass
class AndroidFactory(UiFactory):
    def create_button(self) -> Button:
        return AndroidButton()
    def create_menu(self)->Menu:
        return AndroidMenu()
class IosFactory(UiFactory):
    def create_menu(self) -> Menu:
        return IosMenu()
    def create_button(self) -> Button:
        return IosButton()
class Application:
    def __init__(self,factory:UiFactory):
        self.button=factory.create_button()
        self.menu=factory.create_menu()
    def render(self):
        self.button.render()
        self.menu.show()
def create_app(os_type:str)->Application:
    if os_type=="Android":
        factory= AndroidFactory()
    elif os_type=="IOS":
        factory= IosFactory()
    else:
        raise ValueError("unknow os")
    return Application(factory)
android=create_app("Android")
android.render()
