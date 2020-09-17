import pygame
import sys
import random
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
        self.tube = Items(pygame.image.load('ressource/tube.png'))
        self.needle = Items(pygame.image.load('ressource/needle.png'))
        self.ether = Items(pygame.image.load('ressource/ether.png'))
        self.syringe = Items(pygame.image.load('ressource/emptysquare.png'))
        self.gameover = pygame.image.load('ressource/gameover.png')
        self.escape = pygame.image.load('ressource/escape.png')

    def verifyItemsPlacement(self):
        itemsPlacementList = [self.tube.placement, self.needle.placement, self.ether.placement]
        itemsPlacementList = list(set(itemsPlacementList))
        if len(itemsPlacementList) != 3:
            while len(itemsPlacementList) != 3:
                del itemsPlacementList
                self.tube.placement = Items(pygame.image.load('ressource/tube.png'))
                self.needle.placement = Items(pygame.image.load('ressource/tube.png'))
                self.ether.placement = Items(pygame.image.load('ressource/tube.png'))
                itemsPlacementList = [self.tube.placement, self.needle.placement, self.ether.placement]
                itemsPlacementList = list(set(itemsPlacementList))
        elif len(itemsPlacementList) == 3:
            pass

    def grabItem(self):

        if self.tube.placement == self.hero.placement:
            self.tube.placement = (235, 561)
        else:
            pass

        if self.needle.placement == self.hero.placement:
            self.needle.placement = (280, 561)
        else:
            pass

        if self.ether.placement == self.hero.placement:
            self.ether.placement = (325, 561)
        else:
            pass

    def makeSyringe(self):

        if self.tube.placement == (235, 561) and self.needle.placement == (280, 561) and self.ether.placement == (325, 561):
            self.tube.image = pygame.image.load('ressource/emptysquare.png')
            self.needle.image = pygame.image.load('ressource/emptysquare.png')
            self.ether.image = pygame.image.load('ressource/emptysquare.png')
            self.syringe.image = pygame.image.load('ressource/syringe.png')
            self.syringe.placement = (370, 561)

    def stab(self, board, playable):

        guardianNearbyTiles = [(440, 40), (480, 80)]

        if self.hero.placement in guardianNearbyTiles:
            if self.syringe.placement == (370, 561):
                self.enemy.image = pygame.image.load('ressource/emptysquare.png')
            elif self.syringe.placement != (370, 561):
                board.blit(self.gameover, (0, 0))
                pygame.display.update()
                pygame.time.wait(1500)
                playable == False
                sys.exit()
        else:
            pass
    
    def win(self, board, playable):

        if self.hero.rect.x == 520 and self.hero.rect.y == 40:
                board.blit(self.escape, (0, 0))
                pygame.display.update()
                pygame.time.wait(1500)
                playable == False
                sys.exit()
