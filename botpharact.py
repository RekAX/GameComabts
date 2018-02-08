#import gamebot
import random
class bot():
    botForce = 3
    botagily = 3
    botintutuin = 3
    botendur = 3
    bothp = 90
    def __init__(self,):
        bot_list = ['Terminator','BigBoos','Administrator','Anonymous','BigBeer','Apocalipsis','Gabilolo','Vagoon']
        bot_name = random.choice(bot_list)

    # self.HP = bothp

        print("Your bot definated")
        print("---------",bot_name,"---------")
        print("Force =", self.botForce)
        print("Agility =", self.botagily)
        print("Intuition =", self.botintutuin)
        print("Endurance =", self.botendur)
        print("Health points =", self.bothp)
        print("-------------------------")





if __name__ == "__main__":
    bot()


