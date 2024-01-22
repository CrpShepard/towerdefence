import pygame
import CalcMath

class Enemy(pygame.sprite.Sprite):
    health = 0
    speed = 0
    effect = []
    type = "placeholder"
    current_coords = [0, 0]
    radius = 0
    path = [0, 0]
    damage = 0
    evasion = 0
    defence = 0
    motion_vector = [0, 0]
    reached_path = False

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resource/images/Enemy_Placeholder.png")
        #self.rect = pygame.Rect(0, 0, 50, 50)
        #self.rect.center = (200, 200)

    def draw(self, surface):
        surface.blit(self.image, pygame.Rect(self.current_coords[0], self.current_coords[1], 50, 50))

    def new_path(self):
        self.motion_vector[0], self.motion_vector[1] = CalcMath.normalized_xy(self.current_coords[0], self.current_coords[1], self.path[0], self.path[1])
        self.reached_path = False

    def move(self):
        self.current_coords[0] += self.motion_vector[0] * self.speed
        self.current_coords[1] += self.motion_vector[1] * self.speed

        self.reached_path = CalcMath.ifReachedPath(self.current_coords, self.path, self.motion_vector)

    def death():
        return
    
    def attack():
        return
    
class Conscript(Enemy):
    health = 80
    speed = 3
    type = "infantry"
    radius = 10
    damage = 1
    evasion = 0.05
    defence = 0