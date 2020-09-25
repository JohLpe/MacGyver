import pygame as pg


class Input():

    def __init__(self, x, y, w, h, text):

        self.rect = pg.Rect(x, y, w, h)
        self.textcolor = (255, 255, 255)
        self.font = pg.font.Font('freesansbold.ttf', 20)
        self.textSurface = self.font.render(text, True, self.textcolor)
