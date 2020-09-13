import pygame


class Walls:
    """Class defining the tiles the hero cannot walk on"""

    TILES = []
    MIN_TILE_AXIS_X = 0
    MAX_TILE_AXIS_X = 600
    AXIS_X_INTERVAL = 40

    MIN_TILE_AXIS_Y = 0
    MAX_TILE_AXIS_Y = 600
    AXIS_Y_INTERVAL = 40

    def __init__(self):
        """initialization of a single tile of the board"""
        self.tileAxisXStart = 0
        self.tileAxisYStart = 0
        self.tileAxisXEnd = 40
        self.tileAxisYEnd = 40

    @classmethod
    def defineWallTiles(cls):
        """define tiles with walls that the player cannot walk on"""
        wallTiles = [(80, 40), (320, 40), (360, 40), (160, 80), (200, 80), (240, 80), (320, 80), (360, 80),\
            (440, 80), (520, 80), (80, 120), (160, 120), (200, 120), (320, 120), (80, 160), (160, 160), (400, 160), (440, 160),\
            (480, 160), (80, 200), (120, 200), (160, 200), (240, 200), (320, 200), (440, 200), (480, 200), (120, 240),\
            (240, 240), (320, 240), (360, 240), (40, 280), (200, 280), (240, 280), (280, 280), (320, 280), (360, 280), (440, 280),\
            (480, 280), (520, 280), (40, 320), (120, 320), (160, 320), (200, 320), (320, 320), (320, 360), (400, 360), (440, 360),\
            (480, 360), (80, 400), (160, 400), (200, 400), (240, 400), (320, 400), (400, 400), (240, 440), (280, 440), (320, 440),\
            (360, 440), (400, 440), (480, 440), (520, 440), (80, 480), (120, 480), (160, 480), (240, 480), (320, 480),\
            (400, 480), (160, 520), (320, 520), (480, 520)]
            
        for x in range(cls.MIN_TILE_AXIS_X, cls.MAX_TILE_AXIS_X, cls.AXIS_X_INTERVAL):
            wallTiles.append((x, 0))
            wallTiles.append((x, 560))
        for y in range(cls.MIN_TILE_AXIS_Y, cls.MAX_TILE_AXIS_Y, cls.AXIS_Y_INTERVAL):
            wallTiles.append((0, y))
            wallTiles.append((560, y))
        return wallTiles