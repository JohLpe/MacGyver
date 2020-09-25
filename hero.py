import pygame


class Hero():
    """Class defining MacGyver's attributes"""

    def __init__(self):

        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'A':
                    x = x * 40
                    coordinatesY = y
                    coordinatesX = x
                    placement = (x, y)
                else:
                    pass

        self.image = pygame.image.load('ressource/avatar.png')
        self.step = 40
        self.rect = self.image.get_rect()
        self.rect.x = coordinatesX
        self.rect.y = coordinatesY
        self.placement = placement

    def move_right(self):
        self.rect.x += self.step
        self.rect.y = self.rect.y
        self.placement = (self.rect.x, self.rect.y)

    def move_left(self):
        self.rect.x -= self.step
        self.rect.y = self.rect.y
        self.placement = (self.rect.x, self.rect.y)

    def move_up(self):
        self.rect.y -= self.step
        self.rect.x = self.rect.x
        self.placement = (self.rect.x, self.rect.y)

    def move_down(self):
        self.rect.y += self.step
        self.rect.x = self.rect.x
        self.placement = (self.rect.x, self.rect.y)
