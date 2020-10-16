import pygame as pg
from maze_reader import *
from hero import Hero
from guardian import Guardian


class Board():

    def __init__(self):

        self.caption = pg.display.set_caption("MacGyver Escape")
        self.display = pg.display.set_mode((600, 600))
        self.needle = item_placement()
        self.tube = item_placement()
        self.ether = item_placement()
        self.syringe = letter_to_sprite('I')[1]
        self.guard = Guardian()
        self.hero = Hero()
        self.endGame = False

    def verifyItemsPlacement(self):

        itemsPlcList = [self.tube, self.needle, self.ether]
        itemsPlcList = list(set(itemsPlcList))
        if len(itemsPlcList) != 3:
            while len(itemsPlcList) != 3:
                del itemsPlcList
                self.tube = item_placement()
                self.needle = item_placement()
                self.ether = item_placement()
                itemsPlcList = [self.tube, self.needle, self.ether]
                itemsPlcList = list(set(itemsPlcList))
        elif len(itemsPlcList) == 3:
            pass

    def init_board(self):

        for coords in letter_to_sprite('W'):
            self.display.blit(pg.image.load('ressource/wall.png'), coords)
        for coords in self.hero.playArea:
            self.display.blit(pg.image.load('ressource/floor.png'), coords)
        for coords in letter_to_sprite('I'):
            self.display.blit(pg.image.load('ressource/inventory.png'), coords)
        for coords in letter_to_sprite('U'):
            self.display.blit(pg.image.load('ressource/upstairs.png'), coords)
        for coords in letter_to_sprite('D'):
            self.display.blit(pg.image.load('ressource/dstairs.png'), coords)
        if self.hero.collectAll is False:
            self.display.blit(pg.image.load('ressource/needle.png'),
                              self.needle)
            self.display.blit(pg.image.load('ressource/tube.png'), self.tube)
            self.display.blit(pg.image.load('ressource/ether.png'), self.ether)
        elif self.hero.collectAll:
            self.display.blit(pg.image.load('ressource/syringe.png'),
                              self.syringe)
        for coords in self.guard.plc:
            self.display.blit(self.guard.image, coords)
        self.display.blit(self.hero.image, self.hero.plc)
        if self.hero.plc in self.guard.plcArea and\
                self.hero.collectAll is False:
            self.display.blit(pg.image.load('ressource/gameover.png'), (0, 0))
            self.endGame = True
        if self.hero.plc in letter_to_sprite('U'):
            self.display.blit(pg.image.load('ressource/escape.png'), (0, 0))
            self.endGame = True
        pg.display.flip()
