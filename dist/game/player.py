from game import params, colors
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('game/sprites/birb.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = params.HEIGHT // 2
        self.speedx = 0
        self.speedy = 0
        self.flag_left = False
        self.flag_right = False

    def update(self):
        # updating speed if space pressed
        self.speedy = params.default_speed
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_SPACE]:
            self.speedy = - params.default_speed
        self.rect.y += self.speedy

        # not letting fall or fly away
        if self.rect.bottom > params.HEIGHT:
            self.rect.bottom = params.HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0
