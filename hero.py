import pygame
from floor import Floor
from walls import Walls


class Hero(pygame.sprite.Sprite):
    """Class defining MacGyver's attributes"""

    def __init__(self):
        super().__init__()
        self.step = 40
        self.image = pygame.image.load('ressource/MacAvatar.png')
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 520
        self.placement = (self.rect.x, self.rect.y)

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