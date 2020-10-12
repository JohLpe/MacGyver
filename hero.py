import pygame as pg
from maze_reader import *


class Hero():
    """Class defining MacGyver's attributes"""

    def __init__(self):

        self.image = pg.image.load('ressource/avatar.png')
        self.x = hero_placement()[0]
        self.y = hero_placement()[1]
        self.plc = (self.x, self.y)
        self.invent = []
        self.step = 40
        self.playArea = letter_to_sprite(['F', 'A', 'U', 'D', 'G'])
        self.collectAll = False

    def collect(self, board):

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
            self.collectAll = True
            board.guard.defeat(board)
        else:
            pass

    def move_right(self, board):
        if ((self.x + self.step), self.y) in self.playArea:
            self.x += self.step
            self.y = self.y
            self.plc = (self.x, self.y)
            self.collect(board)

    def move_left(self, board):
        if ((self.x - self.step), self.y) in self.playArea:
            self.x -= self.step
            self.y = self.y
            self.plc = (self.x, self.y)
            self.collect(board)

    def move_up(self, board):
        if (self.x, (self.y - self.step)) in self.playArea:
            self.y -= self.step
            self.x = self.x
            self.plc = (self.x, self.y)
            self.collect(board)

    def move_down(self, board):
        if (self.x, (self.y + self.step)) in self.playArea:
            self.y += self.step
            self.x = self.x
            self.plc = (self.x, self.y)
            self.collect(board)
