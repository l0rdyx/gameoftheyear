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
    mobs = pygame.sprite.Group()
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
    print(params.WIDTH // 200)
    tubes = [tube.Tube(params.WIDTH + 200 * i, random.randint(0, 350)) for i in range(params.WIDTH // 200)]
    l = len(tubes)
    for i in range(l):
        top_tube = tube.Tube(tubes[i].rect.centerx, tubes[i].rect.top - 120 - params.HEIGHT)
        tubes.append(top_tube)
    for s in range(len(tubes) - params.WIDTH // 200):
        all_sprites.add(tubes[s])
        tubes[s].pair = tubes[s + params.WIDTH // 200] #add to par
        all_sprites.add(tubes[s + params.WIDTH // 200])
        mobs.add(tubes[s])
    player_1 = player.Player()
    all_sprites.add(player_1)

    while running:
        clock.tick(params.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Обновление
        all_sprites.update()
        #hits = pygame.sprite.spritecollide(player_1, mobs, False)
        #if hits:
        #   running = False
        # Рендеринг
        screen.fill(colors.BLACK)
        all_sprites.draw(screen)
        print(len(all_sprites))
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()
