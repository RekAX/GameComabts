import pygame
from pygame.locals import *
from Player_1 import *
from monster import *

background_colour = (0,0,0)
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('RPG Game')
screen.fill(background_colour)

pygame.display(starting_money(500), stam(100))
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
