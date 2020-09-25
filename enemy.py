import pygame


class Guardian():
    """Class defining the guardian's attributes"""

    def __init__(self):

        maze = open('maze.txt', 'r')
        for y, line in enumerate(maze):
            y = y * 40
            for x, letter in enumerate(line):
                if x == 15:
                    continue
                if letter == 'G':
                    x = x * 40
                    coordinatesX = x
                    coordinatesY = y
                    placement = (x, y)
                else:
                    pass

        self.image = pygame.image.load('ressource/guardian.png')
        self.rect = self.image.get_rect()
        self.rect.x = coordinatesX
        self.rect.y = coordinatesY
        self.placement = placement
