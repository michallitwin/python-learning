from abc import ABC, abstractmethod
import datetime


class Vehicle(ABC):
    def __init__(self, model, speed, fuel, mileage):
        self.model = model
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    @abstractmethod
    def calculate_range(self, distance):
        pass

    def __str__(self):
        return f" Pojazd o modelu {self.model}, vmax = {self.speed}, fuel = {self.fuel}"
    
class elektryczny(Vehicle):
    def __init__(self, model, speed, fuel, mileage, energy):
        super().__init__(model, speed, fuel, mileage)
        self.energy = energy

    def calculate_range(self, distance):
        return f"Transport o nazwie {self.model} ma zasieg {distance} km"
    
    def check_energy(self):
        if self.energy < 20:
            return f"Pojazd o nazwie {self.model} ma bardzo malo energi - {self.energy} - potrzebne ladowanie"
        return f" Pojazd {self.model} ma {self.energy} energii"
        
    def ladowanie(self, amount):
        self.energy += amount
        return f"Pojazd {self.model} zostal naladowany i ma {self.energy}. Dodano {amount}"
            

class spalinowy(Vehicle):
    def __init__(self, model, speed, fuel, mileage):
        super().__init__(model, speed, fuel, mileage)

    def calculate_range(self, distance):
        return f"Transport o nazwie {self.model} ma zasieg {distance}"

class Car(spalinowy):
    def __init__(self, model, speed, fuel, mileage):
        super().__init__(model, speed, fuel, mileage)

    def calculate_range(self, distance):
        return f"Transport o nazwie {self.model} ma zasieg {distance}"

class Truck(spalinowy):
    def __init__(self, model, speed, fuel, mileage, ladownosc):
        super().__init__(model, speed, fuel, mileage)
        self.ladownosc = ladownosc

    def calculate_range(self, distance):
        return f"Transport o nazwie {self.model} ma zasieg {distance}"
    
    def dodaj_ladunek(self, kgtowar):
        self.ladownosc += kgtowar
        return f" Do pojazdu o modelu {self.model} dodano nowy towar o wadze {kgtowar}. Laczna waga = {self.ladownosc} "

class ElectricVehicle(elektryczny):
    def __init__(self, model, speed, fuel, mileage, energy):
        super().__init__(model, speed, fuel, mileage, energy)

    def calculate_range(self, distance):
        return f"Transport o nazwie {self.model} ma zasieg {distance}"
    


class Weather:
    def __init__(self, typ_pogody, wiatr):
        self.typ_pogody = typ_pogody
        self.wiatr = wiatr
        

    def __str__(self):
        return f"Stan pogody - {self.typ_pogody}, wiatr - {self.wiatr} km/h "
    

    def zagrozenia(self, cel):
        if self.typ_pogody == "burza":
            pass
        if self.typ_pogody == "śnieżyca":
            pass
        if self.typ_pogody == "slonecznie":
            pass






rowerelektryczny = ElectricVehicle('kross', 40,None,None,15)
samochod1 = Car('bmw', 300,'diesel', 15000) 
ciezarowa= Truck('abc', 150, 'gas', 150000, 1000)


print(ciezarowa.dodaj_ladunek(150))
print(samochod1)
print(rowerelektryczny.ladowanie(30))
print(rowerelektryczny.check_energy())
print(samochod1.calculate_range(150))