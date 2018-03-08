import pygame
import sys

from Menu import mainMenu
from StateHandler import *
from Overview import *

# initialize pygame
pygame.init()
winSize = (800, 600)
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("Fire Emblem: Battle System Demo")

clock = pygame.time.Clock()
running = True

stateHandler = StateHandler()

firstState = mainMenu(stateHandler)
overview = overview(stateHandler)

stateHandler.states(firstState, overview)

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user quit?
                 running = False

        keys = pygame.key.get_pressed()
        stateHandler.update()

        clock.tick(60)

pygame.quit() # quit pygame