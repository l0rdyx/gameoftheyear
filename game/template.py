import pygame
import random
from game import colors, params, player


def run():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    pygame.display.set_caption("Shmup!")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player_1 = player.Player()
    all_sprites.add(player_1)
    running = True
    while running:
        clock.tick(params.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Обновление
        all_sprites.update()
        # Рендеринг
        screen.fill(colors.BLACK)
        all_sprites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()
