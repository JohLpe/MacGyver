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

    def move_right(self):
        self.rect.x += self.step

    def move_left(self):
        self.rect.x -= self.step

    def move_up(self):
        self.rect.y -= self.step

    def move_down(self):
        self.rect.y += self.step
    
    def downStairs(self):
        if self.rect.x == 120 and self.rect.y == 520:
            print("I won't escape this place if I go back this way.")
        else:
            pass
