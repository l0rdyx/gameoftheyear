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
        # score if player flying by
        if self.rect.right == 100 and self.pair:
            params.score += 1

        # if tube riches left side of screen, respawning it at the right side with random position
        if self.rect.left < 0:
            # cause we need to respawn both tubes at the same time
            if self.pair:
                new_y = random.randint(0, 350)
                self.rect.bottom = params.HEIGHT + new_y
                print(self.pair.rect.top)
                self.pair.rect.bottom = self.rect.top - 120
                self.rect.left = params.WIDTH - 100
                self.pair.rect.left = params.WIDTH - 100
            print(self.pair.rect.top, ' ', self.pair.rect.centery, ' ', self.pair.rect.bottom)
            print(self.rect.top, ' ', self.rect.centery, ' ', self.rect.bottom)

        # moving tube
        self.rect.x += params.tubes_speed
        self.eye_pos_counter += 1

        # changing eye style every 10 ticks
        if self.eye_pos_counter >= 10:
            self.image = pygame.image.load('game/sprites/tube_2pos.bmp')
            self.eye_pos_counter = 0
        elif self.eye_pos_counter >= 5:
            self.image = pygame.image.load('game/sprites/tube_2pos.bmp')
        else:
            self.image = pygame.image.load('game/sprites/tube_1pos.bmp')

