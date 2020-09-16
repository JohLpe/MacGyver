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

    def __init__(self, image):

        FLOOR = Floor.defineFloorTiles()
        REMOVAL_LIST = [(80, 520), (120, 520), (440, 40), (480, 40), (520, 40), (480, 80)]
        for element in REMOVAL_LIST:
            if element in FLOOR:
                FLOOR.remove(element)
        I = random.randrange(0, len(FLOOR))

        self.image = image
        self.placement = FLOOR.pop(I)
        self.rect = self.image.get_rect()
