import pygame
from Character import *

class map():
    def generateMap(self):
        TILESIZE = 64
        MAPWIDTH = 12
        MAPHEIGHT = 12

        mapsurface = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

        #set values to the assets
        grass = 0
        water = 1
        tree = 2

    	#get assets
        mapAssets ={
    		grass : pygame.image.load("../res/img/grass.png"),
    		water : pygame.image.load("../res/img/ocean.png"),
    		tree : pygame.image.load("../res/img/trees.png"),
            }
    		

    	#maps
        tilemap1 = [ 
    				[grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
                    [grass,grass,grass,grass,grass,grass,tree,grass,grass,grass,grass,grass],
                    [grass,tree,grass,grass,grass,grass,grass,grass,grass,grass,water,grass],
                    [grass,grass,water,grass,grass,grass,grass,grass,grass,grass,grass,grass],
                    [grass,water,water,water,grass,grass,grass,grass,grass,grass,grass,grass],
                    [grass,grass,water,grass,grass,grass,grass,tree,grass,grass,grass,grass],
                    [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
                    [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
                    [grass,grass,grass,tree,tree,grass,grass,grass,grass,grass,tree,grass],
                    [grass,grass,grass,grass,tree,grass,grass,grass,grass,grass,grass,grass],
                    [grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
                    [water,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass,grass],
                ]

        for row in range(MAPHEIGHT):
            for col in range(MAPWIDTH):
                mapsurface.blit(mapAssets[tilemap1[row][col]], (col*TILESIZE, row*TILESIZE))
        pygame.display.update()