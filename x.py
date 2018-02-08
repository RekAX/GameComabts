#!/usr/bin/python
# -*- coding: utf-8 -*-
import hero_pharachter

from botpharact import bot
import random

class accound():
    #login = input("Add your login: ")
    #passwd = input("Add Password: ")
    def __init__ (self):
        print("WELLCOMR")
    def asd(self):

       #getpass.getpass = passwd
       if (self.passwd=="pass"):
           print ("You are Welcome...")

       else:
           print ("Sorry! Your are not allowed.")




class botattack():

    def __init__(self):
        print("Hucum etmek istediyiiniz sahe:..")
        print("hucum etmek instediyiniz hisse: Head, Chest , Pax , Leg ")
        self.hp = bot.bothp



    def att(self):
        int(input("plaease send number: 1 2 3 4 :"))
        self.attmin = 1
        self.attmax = 50
        self.randit = random.randint(self.attmin, self.attmax)
        self.hp = self.hp - self.randit


        if self.randit >= 30:
            print("Critical damage -",self.randit,"Bots Health",self.hp)
            if self.hp<=0:
                print(print("Bot is dead", "Bot's Health :",self.hp))
                return

        elif self.hp <0:
                print("Bot is lose", "Your Damage -",self.randit, "Boths Health :",self.hp)
                return
        else :
                self.randit < 30
                print("normal damage -" ,self.randit ,"Bots Health", self.hp)



    def __call_(self,a):
        self.a = botattack.att()
        self.b = hero_pharachter.ters()





if __name__ == "__main__":
    accound()
    hero_pharachter.hero()
    botattack().att()




