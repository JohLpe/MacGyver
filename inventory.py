import pygame as pg


class Inventory():

    def __init__(self):

        self.sprSize = 40
        self.image = pg.image.load('ressource/inventory.png')

    def invent_tiles(self):

        maze = open('maze.txt', 'r')
        inventoryTiles = []
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == 'I':
                    x = x * self.sprSize
                    inventoryTiles.append((x, y))
        return inventoryTiles
