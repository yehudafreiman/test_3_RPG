from random import randint, choice

class Orc:
    def __init__(self,name:str):
        self.name = name
        self.hp = 50
        self.type = "Orc"
        self.speed = randint(0, 5)
        self.power = randint(10, 15)
        self.armor_rating = randint(2, 8)
        self.weapon = choice(["Knife","Sword","Ax"])

    def speak(self) -> str:
        return f"The {self.type} {self.name} say bla bla"

    def attack(self):
        pass
