
import random
import game
import gamebot
from hero_pharachter import hero
class attack_to_bot():

    def __init__(self):
        self.hp = hero.HP

    def att(self):
        #int(input("plaease send number: 1 dalax  3 4 :"))
        attmin = 1
        attmax = 50
        self.randit = random.randint(attmin,attmax)
        self.hp = self.hp - self.randit
        boed = game.botattack()
        hrone = gamebot.attack_to_bot()

        if self.randit >= 30:
            print("Critical damage -", self.randit, "Your Health", self.hp)
            if self.hp <= 0:
                print(print("Bot is dead", "Your's Health :", self.hp))


        elif self.hp < 0:
            print("Bot is lose", "Your Damage -", self.randit, "Your Health :", self.hp)

        else:

            print("normal damage -", self.randit, "Your Health", self.hp)


            if self.hp > 0:
                boed.att()
                print("YOU ARE DEAD!!!")
            else:
                hrone.att()
                print("sada")


