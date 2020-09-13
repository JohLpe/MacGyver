import pygame


class Enemy(pygame.sprite.Sprite):
    """Class defining the enemy's attributes"""

    def __init__(self):

        self.image = pygame.image.load('ressource/guardian.png')
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 40
        
    def defeated(self):
        pass