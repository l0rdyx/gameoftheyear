import pygame
import random
from game import colors, params, player, tube


def run():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    pygame.display.set_caption("flappy slime!")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    print(params.WIDTH // 50)
    tubes = [tube.Tube(100 * (i + params.WIDTH // 100 // 3), random.randint(0, 450)) for i in range(params.WIDTH // 100)]
    print(tubes)
    for s in tubes:
        all_sprites.add(s)
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
