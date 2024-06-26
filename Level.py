import pygame
import CalcMath
import params
import Tower

class Level(pygame.sprite.Sprite):
    level = 0
    towers = []
    towers_coords = []
    towers_area = []
    tower_cell_size = params.tower_cell_size
    wave_timer = 0
    spawn_rate = 0
    spawn_coords_x = 1225
    enemies = []
    base_coords_x = 25
    #base_lives = 0
    paths = []
    grid = {}
    cell_size = 80
    width = params.game_area_width
    height = params.game_area_height

    def __init__(self, surface):
        super().__init__()
    
        for coord in self.towers_coords:
            self.towers_area.append([pygame.draw.rect(surface, color=(0, 0, 0), rect=pygame.Rect(coord[0], coord[1], self.tower_cell_size, self.tower_cell_size), width=2), False])

    def drawCells(self, surface):
        for i in range(0, self.width, self.cell_size):
            pygame.draw.line(surface, (0,0,0), (i, 0), (i, self.height))
        for i in range(0, self.height+1, self.cell_size):
            pygame.draw.line(surface, (0,0,0), (0, i), (self.width, i)) 

    def drawLevel(self, surface):
        for coord in self.towers_coords:
            pygame.draw.rect(surface, color=(0, 0, 0), rect=pygame.Rect(coord[0], coord[1], self.tower_cell_size, self.tower_cell_size), width=2)
        
        pygame.draw.rect(surface, color=(127, 255, 212), rect=pygame.Rect(0, 0, self.base_coords_x, self.height), width=0) #base outline
        pygame.draw.rect(surface, color=(255, 45, 0), rect=pygame.Rect(self.spawn_coords_x, 0, self.width - self.spawn_coords_x, self.height), width=0) #enemy spawn outline

    def calculateCells(self, obj):
        min_cell_x = int(max(0, (obj.x - obj.radius) // self.cell_size))
        max_cell_x = int(min(self.width // self.cell_size - 1, (obj.x + obj.radius) // self.cell_size))
        min_cell_y = int(max(0, (obj.y - obj.radius) // self.cell_size))
        max_cell_y = int(min(self.height // self.cell_size - 1, (obj.y + obj.radius) // self.cell_size))
        return (min_cell_x, max_cell_x, min_cell_y, max_cell_y)


    def addEnemyToCell(self, enemy):
        min_cell_x, max_cell_x, min_cell_y, max_cell_y = self.calculateCells(enemy)
        for cell_x in range(min_cell_x, max_cell_x + 1):
            for cell_y in range(min_cell_y, max_cell_y + 1):
                cell_key = (cell_x, cell_y)
                if cell_key not in self.grid:
                    self.grid[cell_key] = []
                if enemy not in self.grid[cell_key]:
                    self.grid[cell_key].append(enemy)
                    enemy.prev_cell_keys = self.getCellKeys(enemy)
                    #print('new cell_key',cell_key)

    def getCellKeys(self, obj):
        min_cell_x, max_cell_x, min_cell_y, max_cell_y = self.calculateCells(obj)
        cell_keys = set()
        for cell_x in range(min_cell_x, max_cell_x + 1):
            for cell_y in range(min_cell_y, max_cell_y + 1):
                cell_keys.add((cell_x, cell_y))
        #print('cell_keys', cell_keys)
        return cell_keys
    
    def handlePrevEnemyCell(self, enemy):
        # Удаляем объект из предыдущих клеток
        currentCellKeys = self.getCellKeys(enemy)
        for cell_key in enemy.prev_cell_keys:
            if cell_key in self.grid:
                if cell_key not in currentCellKeys:
                    self.grid[cell_key].remove(enemy)
                    #print('removed enemy from', cell_key)
        enemy.prev_cell_keys = self.getCellKeys(enemy)

    def getEnemyInRadius(self, tower):
        #cell_keys = self.getCellKeys(tower)
        count = 0
        for cell_key in tower.cell_keys:
            if cell_key in self.grid:
                if self.grid[cell_key]:
                    for enemy in self.grid[cell_key]:
                        if CalcMath.isCircleInsideCircle(enemy.x, enemy.y, enemy.radius, tower.x + self.tower_cell_size // 2, tower.y + self.tower_cell_size // 2, tower.radius):
                            if enemy not in tower.targets and enemy.alive:
                                #tower.targets.append(enemy)
                                tower.newEnemy(enemy)
                                count += 1
                                print('target in sight!')
                                if tower.type == Tower.Type.SINGLE:
                                    tower.inSearch = False
                                    return
                            #print('enemy at', cell_key)
                        #elif enemy in tower.targets:
                            #tower.targets.remove(enemy)
                            #tower.deleteEnemy(enemy)

    def trackTargets(self, tower):
        if tower.type == Tower.Type.SINGLE:
            if tower.targets:
                enemy = tower.targets[0]
                if not CalcMath.isCircleInsideCircle(enemy.x, enemy.y, enemy.radius, tower.x + self.tower_cell_size // 2, tower.y + self.tower_cell_size // 2, tower.radius):
                    tower.deleteEnemy(enemy)
                    tower.inSearch = True
                    return
                if not enemy.alive:
                    tower.deleteEnemy(enemy)
                    tower.inSearch = True
            else:
                tower.inSearch = True

    def deleteEnemy(self, enemy):
        cell_keys = self.getCellKeys(enemy)
        for cell_key in cell_keys:
            if cell_key in self.grid:
                if enemy in self.grid[cell_key]:
                    self.grid[cell_key].remove(enemy)

        for tower in self.towers:
            if enemy in tower.targets:
                #tower.targets.remove(enemy)
                tower.deleteEnemy(enemy)

        self.enemies.remove(enemy)

    '''
    def enemyReachedBase(self, enemy):
        self.deleteEnemy(enemy)
        self.base_lives -= enemy.damage
        print('Base lives:', self.base_lives)
        if (self.base_lives < 1):
            print('Game Over!')
    '''

    def initTower(self, tower):
        tower.cell_keys = self.getCellKeys(tower)                 

class Level_Debug(Level):
    level = 0
    towers_coords = [[200, 200], [200, 400]]
    paths = [[0, 360]]

