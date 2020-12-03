import pygame
from game import params


class Menue(pygame.sprite.Sprite):
    def __init__(self, background):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(background)
        self.rect = self.image.get_rect()
        self.rect.centerx = params.WIDTH / 2