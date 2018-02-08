import random
import botpharact
import time
class hero():


    force = 3
    agily = 3
    intutuin = 3
    endur = 3
    HP = 180
    def __init__(self):
        self.hername = input("Hero name: ")
        #self.age = str(input("Your age: "))

        print("Wellcome Sir", self.hername, "Your are")#, self.age)
        print("\n")
        self.health()
        print("Loading Random bot please wait few minutes..")
        time.sleep(2)

        bot_call = botpharact.bot()
        bot_call

        #self.health()


    def health(self):
        print("-------------", self.hername, "------------")
        print("Force =", self.force)
        print("Agility =",self.agily)
        print("Intuition =", self.intutuin)
        print("Endurance =", self.endur)
        print("Health points =", self.HP)
        print("-------------------------")








class ters():


    def __init__(self):
        #print("hucum etmek instediyiniz hisse: Head, Chest , Pax , Leg ")


        self.herohp = hero.HP




    def action(self):
        attack_list = [ 'Head', 'Chest' , 'Pax' , 'Leg']
        attack = int(input(attack_list))

        self.attmin = 1
        self.attmax = 30
        self.randit = random.randint(self.attmin, self.attmax)
        self.herohp = self.herohp - self.randit

        if self.randit >= 20:
            print("Critical damage -", self.randit, "Bots Health", self.herohp)
            if self.herohp <= 0:
                print(print("Bot is dead", "Bot's Health :", self.herohp))
                return

        elif self.herohp < 0:
            print("Bot is lose", "Your Damage -", self.randit, "Boths Health :", self.herohp)
            return
        else:
            self.randit < 20
            print("Normal damage -", self.randit, "Bots Health", self.herohp)





if __name__ == "__main__":
    hero()
