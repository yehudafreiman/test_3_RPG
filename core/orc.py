from random import randint

class Orc:
    def __init__(self,name:str,weapon:str):
        self.name = name
        self.hp = 50
        self.type = "Orc"
        self.speed = randint(0, 5)
        self.power = randint(10, 15)
        self.armor_rating = randint(2, 8)
        self.weapon = randint(1, 3)

    # initialization features
    def set_weapon(self):
        if self.weapon == 1:
            self.weapon = "Knife"
        if self.weapon == 2:
            self.weapon = "Sword"
        if self.weapon == 3:
            self.weapon = "Ax"


    # other methods
    def speak(self) -> str:
        return f"The {self.type} {self.name} say bla bla"

    def attack(self):
        pass
