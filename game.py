import pygame
import sys
from enemy import Guardian
from hero import Hero
from walls import Walls
from floor import Floor
from stairs import Stairs
from items import Items


class Game():

    def __init__(self):
        """class defining the game mecanisms"""

        self.hero = Hero()
        self.enemy = Guardian()
        self.walls = Walls(pygame.image.load('ressource/wall.png'))
        self.floor = Floor(pygame.image.load('ressource/floor.png'))
        self.downstairs = Stairs(pygame.image.load('ressource/downstairs.png'))
        self.upstairs = Stairs(pygame.image.load('ressource/upstairs.png'))
        self.ether = Items(pygame.image.load('ressource/ether.png'))
        self.needle = Items(pygame.image.load('ressource/needle.png'))
        self.tube = Items(pygame.image.load('ressource/tube.png'))
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
                self.needle.placement = Items(pygame.image.load('ressource/needle.png'))
                self.ether.placement = Items(pygame.image.load('ressource/ether.png'))
                itemsPlacementList = [self.tube.placement, self.needle.placement, self.ether.placement]
                itemsPlacementList = list(set(itemsPlacementList))
        elif len(itemsPlacementList) == 3:
            pass

    def grabItem(self):

        if self.tube.placement == self.hero.placement:
            self.tube.placement = (215, 561)
        else:
            pass
        if self.needle.placement == self.hero.placement:
            self.needle.placement = (260, 561)
        else:
            pass
        if self.ether.placement == self.hero.placement:
            self.ether.placement = (305, 561)
        else:
            pass

    def makeSyringe(self):

        if self.tube.placement == (215, 561) and self.needle.placement == (260, 561) and self.ether.placement == (305, 561):
            self.tube.image = pygame.image.load('ressource/emptysquare.png')
            self.needle.image = pygame.image.load('ressource/emptysquare.png')
            self.ether.image = pygame.image.load('ressource/emptysquare.png')
            self.syringe.image = pygame.image.load('ressource/syringe.png')
            self.syringe.placement = (350, 561)

    def stab(self, board, playable):

        dud = Guardian()
        guardianNearbyTiles = [(dud.rect.x + 40, dud.rect.y), \
            (dud.rect.x - 40, dud.rect.y), (dud.rect.x, dud.rect.y + 40), (dud.rect.x, dud.rect.y - 40)]

        if self.hero.placement in guardianNearbyTiles:
            if self.syringe.placement == (350, 561):
                self.enemy.image = pygame.image.load('ressource/emptysquare.png')
            elif self.syringe.placement != (350, 561):
                board.blit(self.gameover, (0, 0))
                pygame.display.update()
                pygame.time.wait(1500)
                playable == False
                sys.exit()
        else:
            pass

    def win(self, board, playable):

        if self.hero.rect.x == self.upstairs.placementXU and self.hero.rect.y == self.upstairs.placementYU:
                board.blit(self.escape, (0, 0))
                pygame.display.update()
                pygame.time.wait(1500)
                playable == False
                sys.exit()