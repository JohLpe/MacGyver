import pygame as pg


def placement():
    sprSize = 40
    maze = open('maze.txt', 'r')
    for y, line in enumerate(maze):
        y = y * sprSize
        for x, letter in enumerate(line):
            if x == 15:
                continue
            if letter == 'A':
                coordX = x * sprSize
                coordY = y
                plc = (coordX, coordY)
                break
    return coordX, coordY, plc


class Hero():
    """Class defining MacGyver's attributes"""

    def __init__(self):

        self.sprSize = 40
        self.image = pg.image.load('ressource/avatar.png')
        self.rect = self.image.get_rect()
        self.step = 40
        self.rect.x = placement()[0]
        self.rect.y = placement()[1]
        self.plc = placement()[2]
        self.invent = []

    def collect(self, board):

        if self.plc == board.needle.plcTuple:
            board.needle.plcTuple = board.inventory.is_inventory()[0]
            self.invent.append('needle')
        elif self.plc == board.tube.plcTuple:
            board.tube.plcTuple = board.inventory.is_inventory()[1]
            self.invent.append('tube')
        elif self.plc == board.ether.plcTuple:
            board.ether.plcTuple = board.inventory.is_inventory()[2]
            self.invent.append('ether')
        if len(self.invent) == 3:
            board.tube.image = pg.image.load('ressource/emptysquare.png')
            board.needle.image = pg.image.load('ressource/emptysquare.png')
            board.ether.image = pg.image.load('ressource/emptysquare.png')
            board.syringe.image = pg.image.load('ressource/syringe.png')
            board.syringe.plc = board.inventory.is_inventory()[1]
            return True
        else:
            return False

    def move(self, board, event):
        if event.key == pg.K_RIGHT:
            move = self.rect.x + self.step
            moveTuple = (move, self.rect.y)
            if moveTuple in board.floor.is_floor():
                self.rect.x += self.step
                self.rect.y = self.rect.y
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        elif event.key == pg.K_LEFT:
            move = self.rect.x - self.step
            moveTuple = (move, self.rect.y)
            if moveTuple in board.floor.is_floor():
                self.rect.x -= self.step
                self.rect.y = self.rect.y
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        elif event.key == pg.K_UP:
            move = self.rect.y - self.step
            moveTuple = (self.rect.x, move)
            if moveTuple in board.floor.is_floor():
                self.rect.y -= self.step
                self.rect.x = self.rect.x
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        elif event.key == pg.K_DOWN:
            move = self.rect.y + self.step
            moveTuple = (self.rect.x, move)
            if moveTuple in board.floor.is_floor():
                self.rect.y += self.step
                self.rect.x = self.rect.x
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        else:
            pass
