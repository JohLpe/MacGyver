import pygame as pg
from maze_elements import Maze
from guard import Guardian
from hero import Hero


class Board():

    def __init__(self):

        self.caption = pg.display.set_caption("MacGyver Escape")
        self.display = pg.display.set_mode((600, 600))
        self.floor = Maze(['F', 'A', 'U', 'D', 'G'])
        self.wall = Maze('W')
        self.upstairs = Maze('U')
        self.downstairs = Maze('D')
        self.inventory = Maze('I')
        # self.needle = Maze(pg.image.load('ressource/needle.png'))
        # self.tube = Maze(pg.image.load('ressource/tube.png'))
        # self.ether = Maze(pg.image.load('ressource/ether.png'))
        # self.syringe = Maze(pg.image.load('ressource/emptysquare.png'))
        self.music = pg.mixer.music.load('ressource/bgst.mp3')
        self.playMusic = pg.mixer.music.play()
        self.guard = Guardian()
        self.hero = Hero()
        # self.gameover = pg.image.load('ressource/gameover.png')
        # self.escape = pg.image.load('ressource/escape.png')
        # self.endGame = False

    # def verifyItemsPlacement(self):

    #     itemsPlcList = [self.tube.plcTuple,
    #                     self.needle.plcTuple, self.ether.plcTuple]
    #     itemsPlcList = list(set(itemsPlcList))
    #     if len(itemsPlcList) != 3:
    #         while len(itemsPlcList) != 3:
    #             del itemsPlcList
    #             self.tube = Maze(pg.image.load('ressource/tube.png'))
    #             self.needle = Maze(pg.image.load('ressource/needle.png'))
    #             self.ether = Maze(pg.image.load('ressource/ether.png'))
    #             itemsPlcList = [self.tube.plcTuple,
    #                             self.needle.plcTuple, self.ether.plcTuple]
    #             itemsPlcList = list(set(itemsPlcList))
    #     elif len(itemsPlcList) == 3:
    #         pass

    def init_board(self, board):

        for coordinates in self.wall.plc:
            self.display.blit(pg.image.load('ressource/wall.png'), coordinates)
        for coordinates in self.floor.plc:
            self.display.blit(pg.image.load('ressource/floor.png'), coordinates)
        for coordinates in self.inventory.plc:
            self.display.blit(pg.image.load('ressource/gameover.png'), coordinates)
        for coordinates in self.upstairs.plc:
            self.display.blit(pg.image.load('ressource/upstairs.png'), coordinates)
        for coordinates in self.downstairs.plc:
            self.display.blit(pg.image.load('ressource/downstairs.png'), coordinates)
        # self.display.blit(self.needle.image, self.needle.plcTuple)
        # self.display.blit(self.tube.image, self.tube.plcTuple)
        # self.display.blit(self.ether.image, self.ether.plcTuple)
        # self.display.blit(self.syringe.image, self.syringe.plcTuple)
        # self.display.blit(self.guard.image, self.guard.guard_tile())
        # self.display.blit(self.hero.image, self.hero.plc)
        # if self.hero.plc in self.ustairs.is_upstairs():
        #     self.display.blit(self.escape, (0, 0))
        #     self.endGame = True
        # if self.guard.defeated(board) is False:
        #     self.display.blit(self.gameover, (0, 0))
        pg.display.flip()

what = Board()
