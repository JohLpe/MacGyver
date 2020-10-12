import pygame as pg
from maze_reader import *


class Guardian():

    def __init__(self):

        self.image = pg.image.load('ressource/guardian.png')
        self.playArea = letter_to_sprite(['F', 'A', 'U', 'D', 'G'])
        self.plc = letter_to_sprite('G')
        self.plcArea = guardian_nearby_tiles()

    def defeat(self, board):

        if board.hero.plc in self.plcArea:
            if board.hero.collectAll:
                self.image = pg.image.load('ressource/empty.png')
