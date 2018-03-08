import pygame

from Map import *
from StateHandler import *

class overview():
    TILESIZE = 64
    MAPWIDTH = 12
    MAPHEIGHT = 12

    mapsurface = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

    def __init__(self, StateHandler):
        self.StateHandler = StateHandler
        #self.sprites = pygame.sprites.Group()

    def update(self):
        map.generateMap(self)
        keys = pygame.key.get_pressed()


