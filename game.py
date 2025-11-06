from random import randint, choice
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin

class Game:
    def start(self):
        while True:
            select = Game.show_menu(self)
            if select:
                print("Start! ->")

                # turn
                player = Game.create_player(self)
                print(f"player -> {player.name}")
                monster = Game.choose_random_monster(self)
                print(f"monster -> {monster.name}")

                player_roll = Game.roll_dice(self,6)
                player_roll += player.speed
                print(f"player result roll -> {player_roll}")
                monster_roll = Game.roll_dice(self,6)
                monster_roll += monster.speed
                print(f"monster result roll -> {monster_roll}")

                if player_roll > monster_roll:
                    current_attacker = player
                elif player_roll < monster_roll:
                    current_attacker = monster
                else:
                    current_attacker = player

                # attack

            else:
                print("End!")
                exit()





    def show_menu(self):
        user_choice = input("Enter fight or quit: ")
        if user_choice == "fight":
            return True
        if user_choice == "quit":
            return False
        else:
            print(f"Invalid input try again {Game.show_menu(self)}")

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

    def roll_dice(self,sides):
        if sides == 6:
            result = randint(0, 6)
        else:
            result = randint(0, 20)
        return result


    def battle(self,player, monster):
        pass






