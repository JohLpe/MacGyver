import pygame as pg


class Walls():

    def __init__(self):

        self.sprSize = 40
        self.image = pg.image.load('ressource/wall.png')

    def wall_tiles(self):
        maze = open('maze.txt', 'r')
        floorCoordinatesList = []
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'W':
                    x = x * self.sprSize
                    floorCoordinatesList.append((x, y))
                else:
                    pass
        return floorCoordinatesList
