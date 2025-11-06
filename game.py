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
                    attacker = player
                    attacked = monster
                elif player_roll < monster_roll:
                    attacker = monster
                    attacked = player
                else:
                    attacker = player
                    attacked = monster
                print(f"current attacker -> {attacker.name}")

                # attack
                while True:
                    attacker_roll = Game.roll_dice(self,20)
                    attacker_roll += attacker.speed
                    if attacker_roll > attacked.armor_rating:
                        print("Hit!")

                        # damage
                        damage = Game.roll_dice(self, 6)
                        damage += attacker.power
                        if attacker == monster:
                            if attacker.weapon == "Knife":
                                damage *= 5
                            elif attacker.weapon == "Sword":
                                damage *= 1
                            else:
                                damage *= 1.5
                        attacked.hp -= damage
                        print(f"current attacked hp -> {attacked.hp}")

                        # state
                        if attacked.hp <= 0:
                            print(f"{attacked.name} is dead!, {attacker.name} win!")
                            print("Game over!")
                            exit()
                    else:
                        print("Miss!")
                        attacker, attacked = attacked, attacker
                        continue
            else:
                print("End!")
                exit()





    def show_menu(self):
        while True:
            user_choice = input("Enter fight or quit: ")
            if user_choice == "fight":
                return True
            if user_choice == "quit":
                return False
            else:
                print(f"Invalid input try again")
                continue

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






