import pygame
from game import params


class Tube(pygame.sprite.Sprite):
    def __init__(self, center, y):
        pygame.sprite.Sprite.__init__(self)
        
        # Alex: does this thing load an image every time tube is created?
        #       if so, i suggest pre-load it
        self.image = pygame.image.load('game/sprites/tube_1pos.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = center
        self.rect.bottom = params.HEIGHT + y
        self.eye_pos_counter = 0

    def update(self):
        if self.rect.left < 0:
            self.rect.left = params.WIDTH
        self.rect.x -= 2
        self.eye_pos_counter += 1
        if self.eye_pos_counter >= 10:
            self.image = pygame.image.load('game/sprites/tube_2pos.bmp')
            self.eye_pos_counter = 0
        elif self.eye_pos_counter >= 5:
            self.image = pygame.image.load('game/sprites/tube_2pos.bmp')
        else:
            self.image = pygame.image.load('game/sprites/tube_1pos.bmp')

