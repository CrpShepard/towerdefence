import pygame

class Level(pygame.sprite.Sprite):
    towers = []
    towers_coords_x = []
    towers_coords_y = []
    towers_area = []
    wave_timer = 0
    spawn_rate = 0
    spawn_coords_x = 0
    enemies = []
    base_coords_x = 0
    base_lives = 0
    paths = []

    def startLevel(self, surface):
        index = 0
        for item in self.towers_coords_x:
            self.towers.append(None)
            self.towers_area.append(pygame.draw.rect(surface, color=(0, 0, 0), rect=pygame.Rect(self.towers_coords_x[index], self.towers_coords_y[index], 50, 50), width=2))
            index += 1
        
        pygame.draw.rect(surface, color=(127, 255, 212), rect=pygame.Rect(0, 0, self.base_coords_x, 720), width=2) #base outline
        pygame.draw.rect(surface, color=(255, 45, 0), rect=pygame.Rect(self.spawn_coords_x, 0, 1280 - self.spawn_coords_x, 720), width=2) #enemy spawn outline


class Level_Debug(Level):
    spawn_coords_x = 1200
    base_coords_x = 50
    base_lives = 999
    towers_coords_x = [100]
    towers_coords_y = [100]
    paths = [0, 360]

