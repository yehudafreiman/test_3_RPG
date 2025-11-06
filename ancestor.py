class Ancestor:
    def __init__(self,name:str,hp:int,speed:int,power:int,armor_rating:int):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating

    def speak(self) -> str:
        pass

    def attack(self):
        pass