from random import randint

class Goblin:
    def __init__(self, name: str, speed: int, power: int, armor_rating: int, weapon: str):
        self.name = name
        self.hp = 20
        self.type = "Goblin"
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = 1
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
        return f"The {self.type} {self.name} say bla bla bla"

    def attack(self):
        pass