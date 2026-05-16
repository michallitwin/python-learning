from abc import ABC, abstractmethod
import datetime
import random




class Vehicle(ABC):
    def __init__(self, model, speed, fuel, mileage, driveable, fuel_consumption, kategoria):
        self.model = model
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.driveable = driveable
        self.fuel_consumption = fuel_consumption
        self.kategoria = kategoria


    @abstractmethod
    def calculate_range(self):
        pass


    def __str__(self):
        return f" Pojazd o modelu {self.model}, vmax = {self.speed}, fuel = {self.fuel}"

class Elektryczny(Vehicle):
    def __init__(self, model, speed, fuel, mileage, energy, driveable, fuel_consumption, energy_consumption, kategoria):
        super().__init__(model, speed, fuel, mileage, driveable, fuel_consumption, kategoria)
        self.energy = energy
        self.energy_consumption = energy_consumption


    def calculate_range(self):
        zasieg = self.energy / self.energy_consumption
        dystans = zasieg * 100
        return f"Elektryk o nazwie {self.model} ma zasieg {dystans} km na energii. Srednie spalanie energii to {self.energy_consumption} kw/h"


    def check_energy(self):
        if self.energy < 20:
            return f"Pojazd o nazwie {self.model} ma bardzo malo energi - {self.energy} - potrzebne ladowanie"
        return f" Pojazd {self.model} ma {self.energy} energii"

    def ladowanie(self, amount):
        self.energy += amount
        return f"Pojazd {self.model} zostal naladowany i ma {self.energy}. Dodano {amount}"



class Spalinowy(Vehicle):
    def __init__(self, model, speed, fuel, mileage, driveable, fuel_consumption, kategoria):
        super().__init__(model, speed, fuel, mileage, driveable, fuel_consumption, kategoria)


    def calculate_range(self):
        zasieg = self.fuel / self.fuel_consumption
        dystans = zasieg * 100
        return f"Transport o nazwie {self.model} ma zasieg {dystans} km"


class Car(Spalinowy):
    def __init__(self, model, speed, fuel, mileage, driveable, fuel_consumption, kategoria):
        super().__init__(model, speed, fuel, mileage, driveable, fuel_consumption, kategoria)


    def calculate_range(self):
        zasieg = self.fuel / self.fuel_consumption
        dystans = zasieg * 100
        return f"Transport o nazwie {self.model} ma zasieg {dystans} km"

class Truck(Spalinowy):
    def __init__(self, model, speed, fuel, mileage, ladownosc, driveable, fuel_consumption, kategoria):
        super().__init__(model, speed, fuel, mileage, driveable, fuel_consumption, kategoria)
        self.ladownosc = ladownosc


    def calculate_range(self):
        zasieg = self.fuel / self.fuel_consumption
        dystans = zasieg * 100
        return f"Transport o nazwie {self.model} ma zasieg {dystans} km"

    def dodaj_ladunek(self, kgtowar):
        self.ladownosc += kgtowar
        return f" Do pojazdu o modelu {self.model} dodano nowy towar o wadze {kgtowar}. Laczna waga = {self.ladownosc} "

class ElectricVehicle(Elektryczny):
    def __init__(self, model, speed, fuel, mileage, energy, driveable, energy_consumption, fuel_consumption, kategoria):
        super().__init__(model, speed, fuel, mileage, energy, driveable, fuel_consumption, energy_consumption, kategoria)        

    def calculate_range(self):
        zasieg = self.energy / self.energy_consumption
        dystans = zasieg * 100
        return f"Elektryk o nazwie {self.model} ma zasieg {dystans} km na energii. Srednie spalanie energii to {self.energy_consumption} kw/h"


class Driver:
    def __init__(self, name, wallet, permissions, tiredness):
        self.name = name
        self.wallet = wallet
        self.permissions = permissions
        self.tiredness = tiredness

    
    def __str__(self):
        return f"Czesc jestem driverem o imieniu {self.name}, mam pozwolenie na kategorie {self.permissions}."

    def naprawa(self, pojazd):
        if pojazd.driveable == False:
            print('Zabieramy sie za naprawe fury, lecz najpierw sprawdzimy srodki')
            if self.wallet >400:
                self.wallet -= 400
                pojazd.driveable = True
                return f"Pojazd udalo sie naprawic "
            else: 
                return f" {self.name} nie masz wystarczajacej ilosci srodkow "
        else:
            return 'Nie jest potrzebna naprawa'


    def sprawdz_prawka(self):
        return f" {self.name} ma prawo jazdy kat : {self.permissions}"
    

    def stan_zmeczenia(self):
        if self.tiredness > 40:
            return f"{self.name} jest zmeczony. Nie powinien siadac za kolko"
        elif self.tiredness > 80:
            return f"{self.name} koniecznie musi pojsc sie przespac!!"
        elif self.tiredness <40:
            return f"{self.name} kierowca moze siadac za kolko"


class FleetManager:
    def __init__(self, nazwa_firmy):
        self.nazwa_firmy = nazwa_firmy
        self.lista_pojazdow = []
        self.lista_kierowcow = []


    def przyjmij_pojazd(self, pojazd):
        self.lista_pojazdow.append(pojazd)
        return f"Do listy pojazdow dodano nowy pojazd - {pojazd}"


    def dodaj_kierowce(self,osoba):
        self.lista_kierowcow.append(osoba)
        return f" Do listy kierowcow dodano nowego kierowce - {osoba}"
    
    def plan_trasy(self, pojazd, trasa, kierowca):
        if kierowca.permissions != pojazd.kategoria:
            return f" {kierowca.name} nie ma prawa jazdy na ten pojazd "
        if pojazd.driveable == False:
            return f"{kierowca.name} - masz zepsuty samochod "
        if kierowca.tiredness > 80:
            return f"Kierowca {kierowca.name} jest wykończony (zmęczenie: {kierowca.tiredness}). Musi iść spać, nie dostanie zlecenia!"
        zasieg_pojazdu = (pojazd.fuel / pojazd.fuel_consumption) * 100
        if trasa > zasieg_pojazdu:
            return f" Kierowca {kierowca.name} nie ma tyle paliwa w baku. Aktualny zasieg to {zasieg_pojazdu}"
        sukces = f" Kierowca {kierowca.name} moze bezpiecznie jechac do celu "
        self.zapisz_zdarzenie(sukces)
        return sukces
    
    def zapisz_zdarzenie(self, wiadomosc):
        with open("logi_floty.txt", 'a') as plik:
            plik.write(f"{wiadomosc}\n")

class Weather:
    def __init__(self, typ_pogody, wiatr):
        self.typ_pogody = typ_pogody
        self.wiatr = wiatr

    def __str__(self):
        return f"Stan pogody - {self.typ_pogody}, wiatr - {self.wiatr} km/h "

    def zagrozenia(self, pojazd):
        if self.typ_pogody == "burza":
            print('Uwaga jest burza - mozliwe uszkodzenie pojazdu')

            szansapiorun = random.randint(1,100)
            if szansapiorun <= 50:
                pojazd.driveable = False
                return f" Pojazd {pojazd.model} zostal uderzony piorunem - potrzebna naprawa "
            else:
                return f" Piorun chybil i trafil w drzewo obok"

        if self.typ_pogody == "sniezyca":
            print('Uwaga jest burza sniezna - mozliwe uszkodzenie pojazdu')

            szansaburza = random.randint(1,100)
            if szansaburza <= 50:
                pojazd.driveable = False
                return f" Lawina uderzyla pojazd o modelu {pojazd.model} - potrzebna naprawa "
            else:
                return f" Lawina przeszla obok - jestes wolny"

        if self.typ_pogody == "slonecznie":
            return f'Bardzo ladna pogoda, wiatr {self.wiatr} km/h - udanej trasy'




boss = FleetManager('Firma')

maciek = Driver('maciek', 502, 'C', 90)
michal1 = Driver('Michal', 500, 'B1', 60)


samochod1= Car('bmw', 350, 50, 150000, True, 15, 'B')
ciezarowka = Truck('abc', 150, 54, 100000, 1000, True, 10, 'CE')
elektryk = ElectricVehicle('toyota', 200, 50, 250000, 52, True, 10, 10, 'B')


pogoda = Weather('burza', 50)



print(boss.plan_trasy(ciezarowka, 150, michal1))

#print(boss.plan_trasy(samochod1, 150, michal1))
#print(boss.przyjmij_pojazd(samochod1))
#print(boss.dodaj_kierowce(michal1))
#print(boss.przyjmij_pojazd(ciezarowka))
#print(pogoda.zagrozenia(samochod1))
#print(michal1.naprawa(samochod1))
#print(michal1.sprawdz_prawka())
#print(michal1)
#print(samochod1.calculate_range())
#print(elektryk.calculate_range())
