from game import params, colors
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('game/sprites/birb.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = params.WIDTH / 2
        self.rect.bottom = params.HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.flag_left = False
        self.flag_right = False

    def update(self):
        if self.flag_left:
            self.speedx -= 0.001
        elif self.flag_right:
            self.speedx += 0.001
        else:
            self.speedx = 0
        self.speedy = 5
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.flag_left = True
            self.flag_right = False
            self.speedx = -8
        if keystate[pygame.K_SPACE]:
            self.speedy = -8
        if keystate[pygame.K_RIGHT]:
            self.flag_left = False
            self.flag_right = True
            self.speedx = 8
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > params.WIDTH:
            self.rect.right = params.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > params.HEIGHT:
            self.rect.bottom = params.HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0
