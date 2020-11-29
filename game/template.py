import pygame
import random
from game import colors, params, player, tube, menue


def run():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    pygame.display.set_caption("flappy slime!")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    menu = menue.Menue()
    all_sprites.add(menu)
    all_sprites.draw(screen)
    pygame.display.flip()
    running = True
    while running:
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame or keystate[pygame.K_RETURN]:
                running = False
                all_sprites.remove(menu)
        pygame.display.update()
        clock.tick(15)
    running = True
    print(params.WIDTH // 50)
    tubes = [tube.Tube(200 * (i + params.WIDTH // 200 // 2), random.randint(0, 350)) for i in range(params.WIDTH // 200)]
    print(tubes)
    for s in tubes:
        all_sprites.add(s)
        all_sprites.add(tube.Tube(s.rect.centerx, s.rect.top - 120 - params.HEIGHT))
    player_1 = player.Player()
    all_sprites.add(player_1)

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
