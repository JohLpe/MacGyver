import random
import pygame
from stairs import Stairs
from hero import Hero
from enemy import Guardian


class Items:
    "class defining the collectable items from the game"

    def __init__(self, image):

        maze = open('maze.txt', 'r')
        hero = Hero()
        en = Guardian()
        guardianNearbyTiles = [(en.rect.x + 40, en.rect.y), \
            (en.rect.x - 40, en.rect.y), (en.rect.x, en.rect.y + 40), (en.rect.x, en.rect.y - 40)]
        stairs = Stairs(pygame.image.load('ressource/emptysquare.png'))
        removalList = [hero.placement, en.placement, stairs.placementD, stairs.placementU]
        removalList.extend(guardianNearbyTiles)
        accessibleTiles = []
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                elif letter == 'F':
                    x = x * 40
                    accessibleTiles.append((x, y))
        for coordinates in removalList:
            if coordinates in accessibleTiles:
                accessibleTiles.remove(coordinates)
        i = random.randrange(0, len(accessibleTiles))

        self.image = image
        self.placement = accessibleTiles[i]
