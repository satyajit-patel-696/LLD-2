from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def printt(self):
        pass


class Oldadopter:
    def write(self):
        print("printiting from old adopter")


class NewPrinter(Printer):
    def printt(self):
        print("printing from new adopter")


class PrinterAdopter(Printer):
    def __init__(self, p: Oldadopter):
        self.p = p

    def printt(self):
        self.p.write()   # ✅ FIXED (removed return)


# Usage
old = Oldadopter()
p = PrinterAdopter(old)

p.printt()