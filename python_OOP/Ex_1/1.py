import random
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, hp, power, defense):
        self.hp =hp
        self.name = name
        self.power = power
        self.defense = defense

    @abstractmethod
    def attack(self, target):
        pass


class Character(Entity):
    
#character ma specjlana metode special ability 
    @abstractmethod
    def special_ability(self, target):
        pass

    @abstractmethod
    def nietrafiony_cios(self, target):
        pass

class Warrior(Character):
    def __init__(self, name, hp, power, defense):
        super().__init__(name, hp, power, defense)

    def attack(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power      
            target.hp -= obrazenia
            return f"{self.name} --- Uderzam target o nazwie {target.name} i zadaje mu {obrazenia} hp. Przeciwnikowi zostaje {target.hp} hp"
    
    def special_ability(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power + 30 
            target.hp -= obrazenia
        return f"{self.name} --- Uderzenie z pol obrotu w przeciwnika {target.name} i zadaje mu {obrazenia} hp. Zostaje mu {target.hp} hp"

    def nietrafiony_cios(self, target):
        return f"{self.name} ---  nie trafil w przeciwnika {target.name}"

class Mage(Character):
    def __init__(self, name, hp, power, defense):
        super().__init__(name, hp, power, defense)

    def attack(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power      
            target.hp -= obrazenia
            return f"{self.name} --- Rzucam kula w przeciwnika o nazwie {target.name} i zadaje mu {obrazenia} hp. Przeciwnikowi zostaje {target.hp} hp"

    def special_ability(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power + 30 
            target.hp -= obrazenia
            return f"{self.name} --- Rzucam OGROMNA KULA W przeciwnika {target.name} i zadaje mu {obrazenia} hp. Zostaje mu {target.hp} hp"
    
    def nietrafiony_cios(self, target):
        return f"{self.name} ---  nie trafil w przeciwnika {target.name}"
    
class Archer(Entity):
    def __init__(self, name, hp, power, defense):
        super().__init__(name, hp, power, defense)   

    def attack(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power      
            target.hp -= obrazenia
            return f"{self.name} --- Strzelam z luku w {target.name} i zadaje mu {obrazenia} hp. Przeciwnikowi zostaje {target.hp} hp"
    

    def special_ability(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power + 30 
            target.hp -= obrazenia
            return f"{self.name} --- Rzucam poteznym harpunem w przeciwnika {target.name} i zadaje mu {obrazenia} hp. Zostaje mu {target.hp} hp"
    
    
    def nietrafiony_cios(self, target):
        return f"{self.name} ---  nie trafil w przeciwnika {target.name}"

class Enemy(Entity):
    def __init__(self, name, hp, power, defense):
        self.hp =hp
        self.name = name
        self.power = power
        self.defense = defense

    @abstractmethod
    def special_attack(self, target):
        pass

class Goblin(Enemy):
    def __init__(self, name, hp, power, defense):
        super().__init__(name, hp, power, defense)

    def attack(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power      
            target.hp -= obrazenia
            return f"{self.name} --- Gryze przeciwnika {target.name} i zadaje mu {obrazenia} hp. Przeciwnikowi zostaje {target.hp} hp"

    def special_attack(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power + 30 
            target.hp -= obrazenia
            return f"{self.name} --- Bardzo mocno gryze przeciwnika {target.name} i zadaje mu {obrazenia} hp. Zostaje mu {target.hp} hp"
    

class Dragon(Enemy):
    def __init__(self, name, hp, power, defense):
        super().__init__(name, hp, power, defense)

    def attack(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power      
            target.hp -= obrazenia
            return f"{self.name} --- Rzucam kule ognia w {target.name} i zadaje mu {obrazenia} hp. Przeciwnikowi zostaje {target.hp} hp"

    def special_attack(self, target):
        if target.hp <=0:
            return f"Przeciwnik {target.name} nie zyje"
        else:
            obrazenia = self.power + 30 
            target.hp -= obrazenia
            return f"{self.name} --- Strzelam OGROMNA KULE w przeciwnika {target.name} i zadaje mu {obrazenia} hp. Zostaje mu {target.hp} hp"
    



class World:
    def __init__(self, heroes, enemies, weather):
        self.heroes = heroes
        self.enemies = enemies
        self.weather = weather
        self.turn_number = 1 


    def save_log(self, message):
        with open("historia_walk.txt", "a") as a:
            a.write(f"{message}\n")


    def start_battle(self):
        print(f"--- Rozpoczynamy bitwe ---\n Pogoda na mapie = {self.weather} ")
        self.save_log("Rozpoczecie walki")

        walka_trwa = True

        while walka_trwa:
            print(f"--- RUNDA {self.turn_number} ---")

            for bohater in self.heroes:

                cel = self.enemies[0]

                rzut_kostka = random.randint(1,3)
                if rzut_kostka == 1:
                    wynik_ataku = bohater.attack(cel)
                elif rzut_kostka == 2:
                    wynik_ataku = bohater.special_attack(cel)
                elif rzut_kostka == 3:
                    wynik_ataku = bohater.nietrafiony_cios(cel)
                print(wynik_ataku)
                self.save_log(wynik_ataku)
                

                if cel.hp <0:
                    walka_trwa = False
                    break
                
            for enemy in self.enemies:

                cel = self.heroes[0]
                rzut_kostka = random.randint(1,2)
                if rzut_kostka == 1:
                    wynik_ataku = enemy.attack(cel)
                elif rzut_kostka == 2:
                    wynik_ataku = enemy.special_ability(cel)
                print(wynik_ataku)
                self.save_log(wynik_ataku)

                if cel.hp <0:
                    walka_trwa = False
                    break


                
            self.turn_number += 1



koks = Warrior('Wojownik',100, 34, 74)
mag= Mage('Magik',100,22, 14)
postac = Archer('Lucznik', 100, 50, 12)

goblinek = Goblin("Goblin", 100, 5, 40)
smok = Dragon("Smok", 300, 250, 50)


#goblinek.special_attack(mag)
#koks.attack(goblinek)
#postac.attack(smok)
#postac.special_ability(goblinek)
#mag.attack(goblinek)


swiat = World([koks, mag], [smok], 'Pochmurnie')
swiat.start_battle()