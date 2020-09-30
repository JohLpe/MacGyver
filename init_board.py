import pygame as pg
from items import Items
from walls import Walls
from floor import Floor
from stairs import Stairs
from guard import Guardian
from hero import Hero
from inputbox import Input


class Board():

    def __init__(self):

        self.caption = pg.display.set_caption("MacGyver Escape")
        self.display = pg.display.set_mode((600, 600))
        self.background = pg.image.load('ressource/void.png')
        self.inventory = pg.image.load('ressource/inventory.png')
        self.music = pg.mixer.music.load('ressource/bgst.mp3')
        self.playMusic = pg.mixer.music.play()
        self.walls = Walls(pg.image.load('ressource/wall.png'))
        self.floor = Floor(pg.image.load('ressource/floor.png'))
        self.downstairs = Stairs(pg.image.load('ressource/downstairs.png'))
        self.guard = Guardian()
        self.hero = Hero()
        self.gameover = pg.image.load('ressource/gameover.png')
        self.escape = pg.image.load('ressource/escape.png')
        self.upstairs = Stairs(pg.image.load('ressource/upstairs.png'))
        self.ether = Items(pg.image.load('ressource/ether.png'),)
        self.needle = Items(pg.image.load('ressource/needle.png'))
        self.tube = Items(pg.image.load('ressource/tube.png'))
        self.syringe = Items(pg.image.load('ressource/emptysquare.png'))

    def verifyItemsPlacement(self):

        itemsPlcList = [self.tube.plc, self.needle.plc, self.ether.plc]
        itemsPlcList = list(set(itemsPlcList))
        if len(itemsPlcList) != 3:
            while len(itemsPlcList) != 3:
                del itemsPlcList
                self.tube = Items(pg.image.load('ressource/tube.png'))
                self.needle = Items(pg.image.load('ressource/needle.png'))
                self.ether = Items(pg.image.load('ressource/ether.png'))
                itemsPlcList = [self.tube.plc, self.needle.plc, self.ether.plc]
                itemsPlcList = list(set(itemsPlcList))
        elif len(itemsPlcList) == 3:
            pass

    def init_board_visual(self, board):

        self.display.blit(self.background, (0, 0))
        for coordinates in self.walls.wall_tiles():
            self.display.blit(self.walls.image, coordinates)
        for coordinates in self.floor.floor_tiles():
            self.display.blit(self.floor.image, coordinates)
        self.display.blit(self.inventory, (210, 562))
        self.display.blit(self.upstairs.image, self.upstairs.plcU)
        self.display.blit(self.downstairs.image, self.downstairs.plcD)
        self.display.blit(self.guard.image, self.guard.guard_tile())
        self.display.blit(self.hero.image, self.hero.plc)
        self.verifyItemsPlacement()
        self.display.blit(self.tube.image, self.tube.plc)
        self.display.blit(self.needle.image, self.needle.plc)
        self.display.blit(self.ether.image, self.ether.plc)
        self.display.blit(self.syringe.image, self.syringe.plc)
        if self.hero.plc == self.upstairs.plcU:
            self.win(board)
        if self.guard.defeated(board) is False:
            self.lose(board)
        else:
            pass
        pg.display.flip()

    def win(self, board):

        restart = Input(200, 400, 180, 36, "Press 'r' to restart")
        quitGame = Input(200, 460, 160, 36, "Press 'q' to quit game")
        self.display.blit(self.escape, (0, 0))
        self.display.blit(restart.textSurface, restart.rect)
        self.display.blit(quitGame.textSurface, quitGame.rect)

    def lose(self, board):
        restart = Input(200, 400, 180, 36, "Press 'r' to restart")
        quitGame = Input(200, 460, 160, 36, "Press 'q' to quit game")
        self.display.blit(self.gameover, (0, 0))
        self.display.blit(restart.textSurface, restart.rect)
        self.display.blit(quitGame.textSurface, quitGame.rect)
