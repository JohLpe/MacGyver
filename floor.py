import pygame
from walls import Walls


class Floor:
    """Class defining tiles the hero can walk on"""

    TILES = []
    MIN_TILE_AXIS_X = 0
    MAX_TILE_AXIS_X = 600
    AXIS_X_INTERVAL = 40

    MIN_TILE_AXIS_Y = 0
    MAX_TILE_AXIS_Y = 600
    AXIS_Y_INTERVAL = 40

    WALLS = Walls.defineWallTiles()

    def __init__(self):
        """initialization of a single tile of the board"""

        self.tileAxisXStart = 0
        self.tileAxisYStart = 0
        self.tileAxisXEnd = 40
        self.tileAxisYEnd = 40

    @classmethod
    def defineFloorTiles(cls):

        floorTiles = []

        for row in range(cls.MIN_TILE_AXIS_X, cls.MAX_TILE_AXIS_X, cls.AXIS_X_INTERVAL):
            for column in range(cls.MIN_TILE_AXIS_Y, cls.MAX_TILE_AXIS_Y, cls.AXIS_Y_INTERVAL):
                if (int(row), int(column)) in cls.WALLS:
                    pass
                else:
                    floorTiles.append((row, column))
        return floorTiles
