#!/usr/bin/python
# -*- coding: utf-8 -*-

import hero_pharachter
import gamebot
import game
from botpharact import bot

import botpharact
import random
import time


#heroman = hero_pharachter.hero


class accound():                                    # Check account

   # login = input("Add your login: ")
   # passwd = input("Add Passw
   # ord: ")
    def __init__ (self):

        print("Password is check")
        time.sleep(1)

    def asd(self):


       #getpass.getpass = passwd
       if (self.passwd=="pass"):
           print ("You are Welcome...")
           #heroman()
       else:
           print ("Sorry! Your are not allowed.")
           exit()
class sentence():                                   #Make proposal figth or shop
    def __init__(self):

        self.send_list =['fight','shop']
        self.send = str(input(self.send_list))
        #print(self.send)
        self.fight = '1'
        self.shop = '2'

        if self.send == self.fight:
            print("Loading to figth...")
            time.sleep(2)
            hero_call = hero_pharachter.hero
            hero_call()


        elif self.send ==self.shop:
            print("Go to Shop...")
            time.sleep(2)
            print("tis shop")
        else:
            print("Wrong answer!!!")
            senten = sentence
            senten()



class terminal():
    def __init__(self):
        self.gots = gamebot.attack_to_bot
        self.bots = game.botattack
        self.hp = bot.bothp


    def atack(self):
        arm = self.gots.att(self)

       # brm = self.bots.att()




        arm(self)
        print("Wait attachk bot")
        time.sleep(2)
      #  brm()
        print("Attack to bot")






if __name__ == "__main__":
    # accound().asd()
    sentence()
    terminal().atack()
     #hero_pharachter.hero()
     #botattack().att()


