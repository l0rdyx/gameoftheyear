import pygame, random
from game import params


class Tube(pygame.sprite.Sprite):
    def __init__(self, center, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('game/sprites/tube_1pos.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = center
        self.rect.bottom = params.HEIGHT + y
        self.eye_pos_counter = 0
        self.pair = None

    def update(self):
        if self.rect.left < 0:
            if self.pair:
                new_y = random.randint(0, 350)
                self.rect.bottom = params.HEIGHT + new_y
                print(self.pair.rect.top)
                self.pair.rect.bottom = self.rect.top - 120
                self.rect.left = params.WIDTH
                self.pair.rect.left = params.WIDTH
            print(self.pair.rect.top, ' ', self.pair.rect.centery, ' ', self.pair.rect.bottom)
            print(self.rect.top, ' ', self.rect.centery, ' ', self.rect.bottom)
            print('очко')
        self.rect.x -= 10
        self.eye_pos_counter += 1
        if self.eye_pos_counter >= 10:
            self.image = pygame.image.load('game/sprites/tube_2pos.bmp')
            self.eye_pos_counter = 0
        elif self.eye_pos_counter >= 5:
            self.image = pygame.image.load('game/sprites/tube_2pos.bmp')
        else:
            self.image = pygame.image.load('game/sprites/tube_1pos.bmp')

