from random import randint

class Player:
    def __init__(self,name:str):
        self.name = name
        self.hp = 50
        self.speed = randint(5,10)
        self.power = randint(5,10)
        self.armor_rating = randint(5,15)
        self.profession = randint(1,2)

    # initialization features
    def set_hp(self):
        if self.profession == "Healer":
            self.hp += 10

    def set_power(self):
        if self.profession == "Warrior":
            self.power += 2

    def set_profession(self):
        if self.profession == 1:
            self.profession = "Healer"
        if self.profession == 2:
            self.profession = "Warrior"

    # other methods
    def speak(self) -> str:
        return f"{self.name} say bla"

    def attack(self):
        pass

