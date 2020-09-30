import pygame as pg


class Hero():
    """Class defining MacGyver's attributes"""

    def __init__(self):

        self.sprSize = 40
        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * self.sprSize
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'A':
                    x = x * self.sprSize
                    coordY = y
                    coordX = x
                    placement = (x, y)
                else:
                    pass
        self.image = pg.image.load('ressource/avatar.png')
        self.rect = self.image.get_rect()
        self.step = 40
        self.rect.x = coordX
        self.rect.y = coordY
        self.plc = placement
        self.invent = []

    def collect(self, board):

        if self.plc == board.needle.plc:
            board.needle.plc = (260, 561)
            self.invent.append('needle')
        elif self.plc == board.tube.plc:
            board.tube.plc = (215, 561)
            self.invent.append('tube')
        elif self.plc == board.ether.plc:
            board.ether.plc = (305, 561)
            self.invent.append('ether')
        if len(self.invent) == 3:
            board.tube.image = pg.image.load('ressource/emptysquare.png')
            board.needle.image = pg.image.load('ressource/emptysquare.png')
            board.ether.image = pg.image.load('ressource/emptysquare.png')
            board.syringe.image = pg.image.load('ressource/syringe.png')
            board.syringe.plc = (350, 561)
            return True
        else:
            return False

    def move(self, board, event):
        if event.key == pg.K_RIGHT:
            move = self.rect.x + self.step
            moveTuple = (move, self.rect.y)
            if moveTuple in board.floor.floor_tiles():
                self.rect.x += self.step
                self.rect.y = self.rect.y
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        elif event.key == pg.K_LEFT:
            move = self.rect.x - self.step
            moveTuple = (move, self.rect.y)
            if moveTuple in board.floor.floor_tiles():
                self.rect.x -= self.step
                self.rect.y = self.rect.y
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        elif event.key == pg.K_UP:
            move = self.rect.y - self.step
            moveTuple = (self.rect.x, move)
            if moveTuple in board.floor.floor_tiles():
                self.rect.y -= self.step
                self.rect.x = self.rect.x
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        elif event.key == pg.K_DOWN:
            move = self.rect.y + self.step
            moveTuple = (self.rect.x, move)
            if moveTuple in board.floor.floor_tiles():
                self.rect.y += self.step
                self.rect.x = self.rect.x
                self.plc = (self.rect.x, self.rect.y)
                self.collect(board)
        else:
            pass
