import pygame
import CalcMath
from dataclasses import dataclass

class Enemy(pygame.sprite.Sprite):
    radius = 12
    health = 0
    speed = 0
    effect = []
    type = 0
    x = 0
    y = 0
    path_x = 0
    path_y = 0
    damage = 0
    evasion = 0
    defence = 0
    motion_vector_x = 0
    motion_vector_y = 0
    reached_path = False

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        #self.image = pygame.image.load("resource/images/Enemy_Placeholder.png")
        #self.rect = pygame.Rect(0, 0, 50, 50)
        #self.rect.center = (200, 200)

    def draw(self, surface):
        #surface.blit(self.image, pygame.Rect(self.x, self.y, 10, 10))
        pygame.draw.circle(surface, (255, 51, 0), (self.x, self.y), self.radius, 0)

    def drawHealthBar(self, surface):
        pass

    def new_path(self):
        self.motion_vector_x, self.motion_vector_y = CalcMath.normalized_xy(self.x, self.y, self.path_x, self.path_y)
        self.reached_path = False

    def move(self):
        self.x += self.motion_vector_x * self.speed
        self.y += self.motion_vector_y * self.speed

        self.reached_path = CalcMath.ifReachedPath(self.x, self.y, self.path_x, self.path_y, self.motion_vector_x, self.motion_vector_y)

    def death():
        return
    
    def attack():
        return
    
class Conscript(Enemy):
    health = 80
    speed = 3
    type = 0
    damage = 1
    evasion = 0.05
    defence = 0