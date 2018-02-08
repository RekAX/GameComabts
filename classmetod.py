#!/usr/bin/python
# -*- coding: utf-8 -*-

import hero_pharachter
from game import botattack
from gamebot import  attack_to_bot
from botpharact import bot

import botpharact
import random
import time


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
            time.sleep(1)
            hero_call = hero_pharachter.hero
            hero_call()
            sentence.hucumlar(self)

        elif self.send ==self.shop:
            print("Go to Shop...")
            time.sleep(2)
            print("tis shop")
        else:
            print("Wrong answer!!!")
            senten = sentence
            senten()


    def hucumlar(self):
        self.hero = botattack().att()
        self.bot = attack_to_bot().att()


if __name__ == "__main__":
    # accound().asd()
    sentence()
