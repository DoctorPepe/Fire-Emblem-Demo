import pygame

"""
StateHandler:
Handles all the given GameStates.
StateHandler handles swapping states and maintaining state
"""

class StateHandler:
    def __init__(self):
        self.stage = 0

    def states(self, mainMenu, overview):
        self.mainMenu = mainMenu
        self.overview = overview
        self.state = self.mainMenu

    def changeState(self, newState):
        self.state = newState

    def update(self):
        self.state.update()

    def goToMainMenu(self):
        self.changeState(self.mainMenu)

    def goToOverview(self):
        self.changeState(self.overview)
