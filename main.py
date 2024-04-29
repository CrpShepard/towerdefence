import pygame
import Tower, Enemy, Level
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

currentLevel = Level.Level_Debug(screen)
tower = Tower.LMG()
enemy = Enemy.Conscript()
currentLevel.enemies.append(enemy)

isTower = False
isTower_showRadius = False

isCurrentLevel_drawCells = True

enemy.x = random.randint(currentLevel.spawn_coords_x, 1280) 
enemy.y = random.randint(0, 720)
enemy.path_x = currentLevel.paths[0]
enemy.path_y = currentLevel.paths[1]
enemy.new_path()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for item in currentLevel.towers_area:
                    if item.collidepoint(event.pos):
                        tower.current_coords = [item.left, item.top]
                        isTower = True
                        isTower_showRadius = True

    for enemy in currentLevel.enemies:
        currentLevel.handleCell(enemy)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    currentLevel.drawLevel(screen)
    enemy.draw(screen)

    if isCurrentLevel_drawCells:
        currentLevel.drawCells(screen)

    if isTower:
        tower.draw(screen)

        if isTower_showRadius:
            tower.showRadius(screen)

        

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