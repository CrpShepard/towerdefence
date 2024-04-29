import pygame

class Level(pygame.sprite.Sprite):
    towers = []
    towers_coords_x = []
    towers_coords_y = []
    towers_area = []
    wave_timer = 0
    spawn_rate = 0
    spawn_coords_x = 1225
    enemies = []
    base_coords_x = 25
    base_lives = 0
    paths = []
    grid = {}
    cell_size = 80
    width = 1280
    height = 560

    def __init__(self, surface):
        index = 0
        for item in self.towers_coords_x:
            self.towers.append(None)
            self.towers_area.append(pygame.draw.rect(surface, color=(0, 0, 0), rect=pygame.Rect(self.towers_coords_x[index], self.towers_coords_y[index], 40, 40), width=2))
            index += 1

    def drawCells(self, surface):
        for i in range(0, self.width, self.cell_size):
            pygame.draw.line(surface, (0,0,0), (i, 0), (i, self.height))
        for i in range(0, self.height+1, self.cell_size):
            pygame.draw.line(surface, (0,0,0), (0, i), (self.width, i)) 

    def drawLevel(self, surface):
        index = 0
        for item in self.towers_coords_x:
            pygame.draw.rect(surface, color=(0, 0, 0), rect=pygame.Rect(self.towers_coords_x[index], self.towers_coords_y[index], 40, 40), width=2)
            index += 1
        
        pygame.draw.rect(surface, color=(127, 255, 212), rect=pygame.Rect(0, 0, self.base_coords_x, 720), width=2) #base outline
        pygame.draw.rect(surface, color=(255, 45, 0), rect=pygame.Rect(self.spawn_coords_x, 0, self.width - self.spawn_coords_x, 720), width=2) #enemy spawn outline

    def handleCell(self, enemy):
        radius_cells = enemy.radius // self.cell_size + 1  # Количество клеток, которые могут быть затронуты радиусом объекта
        min_cell_x = int(max(0, (enemy.x - enemy.radius) // self.cell_size))
        max_cell_x = int(min(self.width // self.cell_size - 1, (enemy.x + enemy.radius) // self.cell_size))
        min_cell_y = int(max(0, (enemy.y - enemy.radius) // self.cell_size))
        max_cell_y = int(min(self.height // self.cell_size - 1, (enemy.y + enemy.radius) // self.cell_size))
        for cell_x in range(min_cell_x, max_cell_x + 1):
            for cell_y in range(min_cell_y, max_cell_y + 1):
                cell_key = (cell_x, cell_y)
                if cell_key not in self.grid:
                    self.grid[cell_key] = []
                    self.grid[cell_key].append(enemy)
                    print(cell_key)

class Level_Debug(Level):
    base_lives = 999
    towers_coords_x = [300]
    towers_coords_y = [300]
    paths = [0, 360]

