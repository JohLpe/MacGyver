import random
import pygame


class Items:
    "class defining the collectable items from the game"

    def __init__(self, image):

        self.sprSize = 40
        self.image = image
        maze = open('maze.txt', 'r')
        accessibleTiles = []
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == 'F':
                    x = x * self.sprSize
                    accessibleTiles.append((x, y))
        i = random.randrange(0, len(accessibleTiles))
        self.plc = accessibleTiles[i]
