import pygame
import Tower, Enemy, Level
import random
import params

# pygame setup
pygame.init()
screen = pygame.display.set_mode((params.screen_width, params.screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

currentLevel = Level.Level_Debug(screen)
tower = Tower.LMG()

isTower_showRadius = False
isCurrentLevel_drawCells = True

for i in range(5):
    enemy = Enemy.Conscript()
    enemy.x = random.randint(currentLevel.spawn_coords_x, params.game_area_width) 
    enemy.y = random.randint(0, params.game_area_height)
    enemy.path_x = currentLevel.paths[0]
    enemy.path_y = currentLevel.paths[1]
    enemy.new_path()
    currentLevel.enemies.append(enemy)

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
                        currentLevel.towers.append(tower)
                        tower.x = item.left
                        tower.y = item.top
                        isTower_showRadius = True
                        tower.built = True

    screen.fill("white")

    currentLevel.drawLevel(screen)
    
    if isCurrentLevel_drawCells:
        currentLevel.drawCells(screen)

    for tower in currentLevel.towers:
        if tower.built:
            tower.draw(screen)
            if isTower_showRadius:
                tower.showRadius(screen)
            currentLevel.getEnemyInRadius(tower)
            tower.update(clock)

    for enemy in currentLevel.enemies:
        enemy.draw(screen)
        currentLevel.addEnemyToCell(enemy)
        currentLevel.handlePrevEnemyCell(enemy)
        enemy.checkHealth()
        if not enemy.alive:
            currentLevel.deleteEnemy(enemy)
        if not enemy.reached_path:
            enemy.move()
        if enemy.x < currentLevel.base_coords_x:
            currentLevel.enemyReachedBase(enemy)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

    dt = clock.tick(60) / 1000
    pygame.display.update()

pygame.quit()