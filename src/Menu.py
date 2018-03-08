import pygame
import sys

from SoundPlayer import SoundPlayer
from Overview import *
from StateHandler import *

class mainMenu():
    def __init__(self, StateHandler):
        self.StateHandler = StateHandler
        self.screen = pygame.display.set_mode((800,600))

    mainMenSound = SoundPlayer().play("mountain_king.ogg")

    def update(self): 
        mainMenImage = pygame.image.load("../res/img/lyn.png")
        BACKGROUND_COLOR = (255, 119, 0)
        BLUE = (29, 20, 155)
        LIGHT_BLUE = (70, 63, 170)

        self.screen.fill(BACKGROUND_COLOR)
        menuTextLarge = pygame.font.SysFont('helvetica.ttf', 72)
        menuTextSmall = pygame.font.SysFont('helvetica.ttf', 32)
        menuTextMain = menuTextLarge.render('Fire Emblem Demo', False, (0,0,0))

        self.screen.blit(menuTextMain,(100,100))
        self.screen.blit(mainMenImage,(100,170))

        pygame.draw.rect(self.screen, BLUE, (150,350,100,50))
        pygame.draw.rect(self.screen, BLUE, (550,350,100,50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 250 > mouse[0] > 150 and 400 > mouse[1] > 350:
            pygame.draw.rect(self.screen, LIGHT_BLUE,(150,350,100,50))
            if click[0] == 1:
                self.StateHandler.goToOverview()

        if 650 > mouse[0] > 550 and 400 > mouse[1] > 350:
            pygame.draw.rect(self.screen, LIGHT_BLUE, (550,350,100,50))
            if click[0] == 1:
                pygame.quit()
                quit()

        playText = menuTextSmall.render('Play', False,(0,0,0))
        quitText = menuTextSmall.render('Quit', False,(0,0,0))
        self.screen.blit(playText,(180,365))
        self.screen.blit(quitText,(580,365))

        pygame.display.flip() # flip the double buffer

       