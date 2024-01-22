import pygame
import Tower, Enemy, Level
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

Level_debug = Level.Level_Debug()
tower = Tower.Tower()
enemy = Enemy.Conscript()

isTower = False

enemy.current_coords = [random.randint(Level_debug.spawn_coords_x, 1280), random.randint(0, 720)]
enemy.path = Level_debug.paths
enemy.new_path()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for item in Level_debug.towers_area:
                    if item.collidepoint(event.pos):
                        tower.current_coords = [item.left, item.top]
                        isTower = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    Level_debug.startLevel(screen)
    enemy.draw(screen)

    if isTower:
        tower.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    if not enemy.reached_path:
        enemy.move()

    dt = clock.tick(60) / 1000
    pygame.display.update()

pygame.quit()