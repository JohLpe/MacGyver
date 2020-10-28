import pygame as pg
from maze_reader import *


class Hero():
    """Class defining MacGyver's attributes."""

    def __init__(self):
        """Class constructor."""

        self.image = pg.image.load('ressource/avatar.png')
        self.x = hero_placement()[0]
        self.y = hero_placement()[1]
        self.plc = (self.x, self.y)
        self.invent = []
        self.step = 40
        self.play_area = letter_to_sprite(['F', 'A', 'U', 'D', 'G'])
        self.collect_all = False

    def collect(self, board):
        """Changes items placements.

        If player encounters an item while moving, item will
        be moved to the player's inventory.

        """

        if self.plc == board.needle:
            board.needle = letter_to_sprite('I')[0]
            self.invent.append('needle')
        elif self.plc == board.tube:
            board.tube = letter_to_sprite('I')[1]
            self.invent.append('tube')
        elif self.plc == board.ether:
            board.ether = letter_to_sprite('I')[2]
            self.invent.append('ether')
        if len(self.invent) == 3:
            self.collect_all = True
            board.guard.defeat(board)
        else:
            pass

    def move_right(self, board):
        """Moves player on the X axis, right direction."""

        if ((self.x + self.step), self.y) in self.play_area:
            self.x += self.step
            self.y = self.y
            self.plc = (self.x, self.y)
            self.collect(board)

    def move_left(self, board):
        """Moves player on the X axis, left direction."""

        if ((self.x - self.step), self.y) in self.play_area:
            self.x -= self.step
            self.y = self.y
            self.plc = (self.x, self.y)
            self.collect(board)

    def move_up(self, board):
        """Moves player on the Y axis, up direction."""

        if (self.x, (self.y - self.step)) in self.play_area:
            self.y -= self.step
            self.x = self.x
            self.plc = (self.x, self.y)
            self.collect(board)

    def move_down(self, board):
        """Moves player on the Y axis, down direction."""

        if (self.x, (self.y + self.step)) in self.play_area:
            self.y += self.step
            self.x = self.x
            self.plc = (self.x, self.y)
            self.collect(board)
