#!/usr/bin/python
# -*- coding: utf-8 -*-
#from botpharact import bot
import botpharact as bot

import random
import gamebot
import hero_pharachter


class botattack():

    def __init__(self):
        print("Hucum etmek istediyiiniz sahe:..")
        print("hucum etmek instediyiniz hisse: Head, Chest , Pax , Leg ")
        self.herohp = bot.bot.bothp
       # print(self.herohp)

    def att(self):
        int(input("plaease send number: 1 2 3 4 :"))
        self.attmin = 1
        self.attmax = 50
        self.randit = random.randint(self.attmin, self.attmax)
        self.herohp = self.herohp - self.randit
        hrone = gamebot.attack_to_bot()


        if self.randit >= 30:
            print("Critical damage -",self.randit,"Bots Health",self.herohp)
            if self.herohp<=0:
                print(print("Bot is dead", "Bot's Health :",self.herohp))
                return


        elif self.herohp <0:
                print("Bot is lose", "Your Damage -",self.randit, "Boths Health :",self.herohp)
                return
        else :
                #self.randit < 30
                print("normal damage -" ,self.randit ,"Bots Health", self.herohp)
                if self.herohp > 0:++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    hrone.att()
                    print("NEse")
                else:
                    print("Boot is lose")