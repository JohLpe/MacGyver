import pygame
import random
from floor import Floor

class Items:
    "class defining the collectable items from the game"

    MIN_TILE_AXIS_X = 0
    MAX_TILE_AXIS_X = 600
    AXIS_X_INTERVAL = 40

    MIN_TILE_AXIS_Y = 0
    MAX_TILE_AXIS_Y = 600
    AXIS_Y_INTERVAL = 40

    FLOOR = Floor.defineFloorTiles()

    def __init__(self, image):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    @classmethod
    def randomPlacement(cls):
        pass