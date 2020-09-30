import pygame as pg


class Floor():

    def __init__(self):

        self.sprSize = 40
        self.image = pg.image.load('ressource/floor.png')

    def floor_tiles(self):

        maze = open('maze.txt', 'r')
        floorCoordinatesList = []
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == 'F':
                    x = x * self.sprSize
                    floorCoordinatesList.append((x, y))
                elif letter == 'A':
                    x = x * self.sprSize
                    floorCoordinatesList.append((x, y))
                elif letter == 'G':
                    x = x * self.sprSize
                    floorCoordinatesList.append((x, y))
                elif letter == 'U':
                    x = x * self.sprSize
                    floorCoordinatesList.append((x, y))
                elif letter == 'D':
                    x = x * self.sprSize
                    floorCoordinatesList.append((x, y))
                else:
                    pass
        return floorCoordinatesList
