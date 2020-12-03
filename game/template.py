import pygame
import random
from game import colors, params, player, tube, menue


def run():
    # init screen and mixer
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    pygame.display.set_caption("flappy slime!")
    clock = pygame.time.Clock()

    # init sprite groups and menue object
    all_sprites = pygame.sprite.Group()
    menu = menue.Menue()
    mobs = pygame.sprite.Group()

    # adding menue and drawing it
    all_sprites.add(menu)
    all_sprites.draw(screen)
    pygame.display.flip()

    # menue running, if enter pressed - cont
    running = True
    while running:
        key_state = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame or key_state[pygame.K_RETURN]:
                running = False
                all_sprites.remove(menu)
        pygame.display.update()
        clock.tick(15)

    # bottom tubes list
    tubes = [tube.Tube(params.WIDTH + 200 * i, random.randint(0, 350)) for i in range(params.tubes_amount)]

    # adding same amount of top tubes
    amount = len(tubes)
    for i in range(amount):
        top_tube = tube.Tube(tubes[i].rect.centerx, tubes[i].rect.top - 120 - params.HEIGHT)
        tubes.append(top_tube)

    # connecting top and bottom tubes and adding all to sprite list
    for s in range(len(tubes) - params.tubes_amount):
        all_sprites.add(tubes[s])
        tubes[s].pair = tubes[s + params.tubes_amount] #add to par
        all_sprites.add(tubes[s + params.tubes_amount])
        mobs.add(tubes[s])

    # adding player
    player_1 = player.Player()
    all_sprites.add(player_1)

    # running game itself
    running = True
    while running:
        clock.tick(params.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update all sprites
        all_sprites.update()

        # quit if player hit the tube
        hits = pygame.sprite.spritecollide(player_1, mobs, False)
        if hits:
            running = False

        # render
        screen.fill(colors.BLACK)
        all_sprites.draw(screen)

        # rendering game score
        font = pygame.font.Font(None, 74)
        text = font.render(str(params.score), 1, colors.WHITE)
        screen.blit(text, (params.WIDTH - 50, 10))

        # flipping rendered screen
        pygame.display.flip()

    pygame.quit()
