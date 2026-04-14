from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def printt(self,txt):
        pass


class Oldadopter:
    def write(self,txt):
        print(f"printiting from old adopter {txt}")


class NewPrinter(Printer):
    def printt(self,txt):
        print(f"printing from new adopter{txt}")


class PrinterAdopter(Printer):
    def __init__(self, p: Oldadopter):
        self.p = p

    def printt(self,txt):
        self.p.write(txt)   # ✅ FIXED (removed return)


# Usage
old = Oldadopter()
p = PrinterAdopter(old)

p.printt("bhula")