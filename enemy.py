import pygame as pg


class Guardian():
    """Class defining the guardian's attributes"""

    def __init__(self):

        self.image = pg.image.load('ressource/guardian.png')
        self.sprSize = 40

    def guardian_tile(self):

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

    def guardian_axis(self):

        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'G':
                    x = x * self.sprSize
                    coordX = x
                    coordY = y
                else:
                    pass
        return coordX, coordY

    def guardian_nearby_tiles(self):

        nearbyTiles = []
        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'G':
                    x = x * self.sprSize
                if letter != 'G':
                    continue
                minX = x - self.sprSize
                maxX = x + (self.sprSize * 2)
                minY = y - self.sprSize
                maxY = y + (self.sprSize * 2)
                for y2 in range(minY, maxY, self.sprSize):
                    for x2 in range(minX, maxX, self.sprSize):
                        nearbyTiles.append((x2, y2))
        return nearbyTiles
