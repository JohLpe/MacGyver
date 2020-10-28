import pygame as pg
from maze_reader import *


class Guardian():
    """Class defining the ennemy's attributes."""

    def __init__(self):
        """Class constructor."""

        self.image = pg.image.load('ressource/guardian.png')
        self.plc = letter_to_sprite('G')
        self.plc_area = guardian_nearby_tiles()

    def defeat(self, board):
        """Changes the image displayed for ennemy if defeated."""

        if board.hero.plc in self.plc_area:
            if board.hero.collect_all:
                self.image = pg.image.load('ressource/empty.png')
