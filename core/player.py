from random import randint, choice

class Player:
    def __init__(self,name:str):
        self.name = name
        self.speed = randint(5,10)
        self.armor_rating = randint(5,15)
        self.profession = choice(["Healer","Warrior"])

        self.hp = 50
        if self.profession == "Healer":
            self.hp += 10

        self.power = randint(5,10)
        if self.profession == "Warrior":
            self.power += 2

    def speak(self) -> str:
        return f"{self.name} say bla"

    def attack(self):
        pass

