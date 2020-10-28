import pygame as pg
from maze_reader import *
from hero import Hero
from guardian import Guardian


class Board():
    """Class for graphic display."""

    def __init__(self):
        """Class constructor."""

        self.caption = pg.display.set_caption("MacGyver Escape")
        self.display = pg.display.set_mode((600, 600))
        self.needle = item_placement()
        self.tube = item_placement()
        self.ether = item_placement()
        self.syringe = letter_to_sprite('I')[1]
        self.guard = Guardian()
        self.hero = Hero()
        self.end_game = False

    def verify_items_placement(self):
        """Verify that items aren't at the same coordinates."""

        items_plc_list = [self.tube, self.needle, self.ether]
        items_plc_list = list(set(items_plc_list))
        if len(items_plc_list) != 3:
            while len(items_plc_list) != 3:
                del items_plc_list
                self.tube = item_placement()
                self.needle = item_placement()
                self.ether = item_placement()
                items_plc_list = [self.tube, self.needle, self.ether]
                items_plc_list = list(set(items_plc_list))
        elif len(items_plc_list) == 3:
            pass

    def init_board(self):
        """display all graphic elements of the game."""

        for coords in letter_to_sprite('W'):
            self.display.blit(pg.image.load('ressource/wall.png'), coords)
        for coords in self.hero.play_area:
            self.display.blit(pg.image.load('ressource/floor.png'), coords)
        for coords in letter_to_sprite('I'):
            self.display.blit(pg.image.load('ressource/inventory.png'), coords)
        for coords in letter_to_sprite('U'):
            self.display.blit(pg.image.load('ressource/upstairs.png'), coords)
        for coords in letter_to_sprite('D'):
            self.display.blit(pg.image.load('ressource/dstairs.png'), coords)
        if not self.hero.collect_all:
            self.display.blit(pg.image.load('ressource/needle.png'),
                              self.needle)
            self.display.blit(pg.image.load('ressource/tube.png'), self.tube)
            self.display.blit(pg.image.load('ressource/ether.png'), self.ether)
        elif self.hero.collect_all:
            self.display.blit(pg.image.load('ressource/syringe.png'),
                              self.syringe)
        for coords in self.guard.plc:
            self.display.blit(self.guard.image, coords)
        self.display.blit(self.hero.image, self.hero.plc)
        if self.hero.plc in self.guard.plc_area and not\
                self.hero.collect_all:
            self.display.blit(pg.image.load('ressource/gameover.png'), (0, 0))
            self.end_game = True
        if self.hero.plc in letter_to_sprite('U'):
            self.display.blit(pg.image.load('ressource/escape.png'), (0, 0))
            self.end_game = True
        pg.display.flip()
