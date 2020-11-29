import pygame
from game import params


class Tube(pygame.sprite.Sprite):
    def __init__(self, center, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('game/tube.bmp')
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centerx = center
        self.rect.bottom = params.HEIGHT + y

    def update(self):
        if self.rect.left < 0:
            self.rect.left = params.WIDTH
        self.rect.x -= 4