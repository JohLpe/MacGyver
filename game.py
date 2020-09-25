import pygame as pg
import sys
from enemy import Guardian
from hero import Hero
from walls import Walls
from floor import Floor
from stairs import Stairs
from items import Items
from inputbox import Input


class Game():

    def __init__(self):
        """class defining the game mecanisms"""

        self.hero = Hero()
        self.enemy = Guardian()
        self.walls = Walls(pg.image.load('ressource/wall.png'))
        self.floor = Floor(pg.image.load('ressource/floor.png'))
        self.downstairs = Stairs(pg.image.load('ressource/downstairs.png'))
        self.upstairs = Stairs(pg.image.load('ressource/upstairs.png'))
        self.ether = Items(pg.image.load('ressource/ether.png'))
        self.needle = Items(pg.image.load('ressource/needle.png'))
        self.tube = Items(pg.image.load('ressource/tube.png'))
        self.syringe = Items(pg.image.load('ressource/emptysquare.png'))
        self.gameover = pg.image.load('ressource/gameover.png')
        self.escape = pg.image.load('ressource/escape.png')
        self.restart = pg.image.load('ressource/restart.png')
        self.quitGame = pg.image.load('ressource/quit.png')

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

    def grabItem(self):

        if self.tube.plc == self.hero.plc:
            self.tube.plc = (215, 561)
        else:
            pass
        if self.needle.plc == self.hero.plc:
            self.needle.plc = (260, 561)
        else:
            pass
        if self.ether.plc == self.hero.plc:
            self.ether.plc = (305, 561)
        else:
            pass

    def makeSyringe(self):

        if self.tube.plc == (215, 561) and self.needle.plc == (260, 561)\
                 and self.ether.plc == (305, 561):
            self.tube.image = pg.image.load('ressource/emptysquare.png')
            self.needle.image = pg.image.load('ressource/emptysquare.png')
            self.ether.image = pg.image.load('ressource/emptysquare.png')
            self.syringe.image = pg.image.load('ressource/syringe.png')
            self.syringe.plc = (350, 561)

    def stab(self, board, event, playable):

        restart = Input(200, 400, 180, 36, "Press 's' to restart")
        quitGame = Input(200, 460, 160, 36, "Press 'q' to quit game")
        endGame = False
        if self.hero.plc in self.enemy.guardian_nearby_tiles():
            if self.syringe.plc == (350, 561):
                self.enemy.image = pg.image.load('ressource/emptysquare.png')
            if self.syringe.plc != (350, 561):
                endGame = True
                while endGame:
                    board.blit(self.gameover, (0, 0))
                    board.blit(restart.textSurface, restart.rect)
                    board.blit(quitGame.textSurface, quitGame.rect)
                    pg.display.update()
                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_a or event.key == pg.K_q:
                                endGame = False
                                sys.exit()
                            else:
                                pass
        else:
            pass

    def win(self, board, event, playable):

        restart = Input(200, 400, 180, 36, "Press 's' to restart")
        quitGame = Input(200, 460, 160, 36, "Press 'q' to quit game")
        gameEnd = False

        if self.hero.rect.x == self.upstairs.placementXU \
                and self.hero.rect.y == self.upstairs.placementYU:
            gameEnd = True
            while gameEnd:
                board.blit(self.escape, (0, 0))
                board.blit(restart.textSurface, restart.rect)
                board.blit(quitGame.textSurface, quitGame.rect)
                pg.display.update()
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_a or event.key == pg.K_q:
                            sys.exit()
                        else:
                            pass
