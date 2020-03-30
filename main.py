import pygame
from game import Game

pygame.init()

# generate window
pygame.display.set_caption("North Crew")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

game = Game(screen)

running = True
while running:

    # load background
    screen.blit(background, (0, -200))

    # load player
    screen.blit(game.player.image, game.player.rect)

    # get all projectiles and make them move
    for projectile in game.player.all_projectiles:
        projectile.move()

    # get all monsters and make them move
    for monster in game.all_monsters:
        monster.forward()

    # draw all projectiles on screen
    game.player.all_projectiles.draw(screen)

    # draw all monsters on screen
    game.all_monsters.draw(screen)

    # moving player left or right
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.mov_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.mov_left()

    pygame.display.flip()

    for event in pygame.event.get():
        # exit event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # moving player
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # if space is pressed to launch projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
