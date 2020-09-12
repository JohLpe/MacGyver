import pygame
from hero import Hero
from enemy import Enemy
from walls import Walls
from floor import Floor
from items import Items

class Game:
    """Class importing elements from other classes for the game to work"""

    def __init__(self):
        """import classes needed for the game"""

        self.hero = Hero()
        self.enemy = Enemy()
        self.walls = Walls()
        self.floor = Floor()
        self.tube = Items(pygame.image.load('ressource/tube.png'), )
        self.needle = Items(pygame.image.load('ressource/needle.png'))
        self.ether = Items(pygame.image.load('ressource/ether.png'))
        # self.syringe = Items(pygame.image.load('ressource/syringe.png'))