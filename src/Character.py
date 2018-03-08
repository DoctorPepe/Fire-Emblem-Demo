import pygame
from SoundPlayer import SoundPlayer
from Map import *

class Character(pygame.sprite.Sprite):
    TILESIZE = 64

    def __init__(self, width, height, image):
        super().__init__() # call the super constructor for the pygame sprite class

        self.image = pygame.image.load("../res/img/" + image)
        self.image = pygame.image.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()

        self.rect.x = 64
        self.rect.y = 64

    def move(self, moveX, moveY):
        self.rect.x += (moveX * TILESIZE)
        self.rect.y += (moveY * TILESIZE)
