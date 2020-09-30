import pygame as pg


class Guardian():
    """Class defining the guardian's attributes"""

    def __init__(self):

        self.image = pg.image.load('ressource/guardian.png')
        self.sprSize = 40

    def guard_tile(self):

        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'G':
                    x = x * self.sprSize
                    placement = (x, y)
                else:
                    pass
        return placement

    def guard_nearby_tiles(self):

        nearbyTiles = []
        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter != 'G':
                    continue
                if letter == 'G':
                    x = x * self.sprSize
                    minX = x - self.sprSize
                    maxX = x + (self.sprSize * 2)
                    minY = y - self.sprSize
                    maxY = y + (self.sprSize * 2)
                    for y2 in range(minY, maxY, self.sprSize):
                        for x2 in range(minX, maxX, self.sprSize):
                            nearbyTiles.append((x2, y2))
        return nearbyTiles

    def defeated(self, board):
        if board.hero.plc in self.guard_nearby_tiles():
            if board.hero.collect(board) is True:
                self.image = pg.image.load('ressource/emptysquare.png')
                return True
            else:
                return False
