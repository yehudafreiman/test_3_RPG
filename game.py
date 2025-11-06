from random import randint, choice
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin

class Game:

    def start(self):
        pass

    def show_menu(self):
        user_choice = input("Enter 'fight' or 'quit'")
        return user_choice

    def create_player(self):
        player = Player("Harry Potter")
        return player


    def choose_random_monster(self):
        monster = choice(["Orc", "Goblin"])
        if monster == Orc:
            monster = Orc("Charizard")
        else:
            monster = Goblin("Alakazam")
        return monster

    def battle(self,player, monster):
        pass

    def roll_dice(self,sides):
        if sides == 6:
            result = randint(0, 6)
        else:
            result = randint(0, 20)





