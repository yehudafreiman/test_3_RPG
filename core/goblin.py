from random import randint, choice

class Goblin:
    def __init__(self, name: str):
        self.name = name
        self.hp = 20
        self.type = "Goblin"
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = 1
        self.weapon = choice(["Knife","Sword","Ax"])

    def speak(self) -> str:
        return f"The {self.type} {self.name} say bla bla bla"

    def attack(self):
        pass

