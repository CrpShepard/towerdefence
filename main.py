import pygame
import Tower, Enemy, Level, PlayerStats, UI
import random
import params

# pygame setup
pygame.init()
screen = pygame.display.set_mode((params.screen_width, params.screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

currentLevel = Level.Level_Debug(screen)
playerStats = PlayerStats.PlayerStats()
playerStats.init(currentLevel.level)
ui = UI.UI()
#ui.drawUI(screen)
ui.updateHealth(playerStats.base_lives)
ui.updateGold(playerStats.gold)

for i in range(1000):
    enemy = Enemy.Conscript()
    enemy.x = random.randint(currentLevel.spawn_coords_x, params.game_area_width) 
    enemy.y = random.randint(0, params.game_area_height)
    enemy.path_x = currentLevel.paths[0][0]
    enemy.path_y = currentLevel.paths[0][1]
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
                    if item[0].collidepoint(event.pos) and not item[1]:
                        item[1] = True
                        tower = Tower.LMG()
                        currentLevel.towers.append(tower)
                        tower.x = item[0].left
                        tower.y = item[0].top
                        currentLevel.initTower(tower)
                        tower.built = True
                        print('Tower has been built!')

    screen.fill("white")

    currentLevel.drawLevel(screen)
    currentLevel.drawCells(screen)

    for tower in currentLevel.towers:
        if tower.built:
            tower.draw(screen)
            tower.showRadius(screen)
            if tower.inSearch:
                currentLevel.getEnemyInRadius(tower)
            else:
                currentLevel.trackTargets(tower)
            if tower.engaged:
                tower.update(clock)

    for enemy in currentLevel.enemies:
        enemy.draw(screen)
        currentLevel.addEnemyToCell(enemy)
        currentLevel.handlePrevEnemyCell(enemy)
        #enemy.checkHealth()
        if not enemy.alive:
            playerStats.receiveGold(enemy.value)
            ui.updateGold(playerStats.gold)
            currentLevel.deleteEnemy(enemy)
        if not enemy.reached_path:
            enemy.move()
        if enemy.x < currentLevel.base_coords_x:
            #currentLevel.enemyReachedBase(enemy)
            playerStats.receiveDamage(enemy.damage)
            ui.updateHealth(playerStats.base_lives)
            currentLevel.deleteEnemy(enemy)

    ui.drawUI(screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

    dt = clock.tick(60) / 1000
    pygame.display.update()

pygame.quit()