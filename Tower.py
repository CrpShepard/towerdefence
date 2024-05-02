import pygame
import params
from enum import Enum

class Type(Enum):
    SINGLE = 0
    MULTIPLE = 1
    AOE = 2

class Tower(pygame.sprite.Sprite):
    damage = 0
    radius = 0
    speed = 0
    effect = []
    type = 0
    cost = 0
    time_to_build = 0
    x = 0
    y = 0
    accuracy = 0
    targets = []
    engage = False
    built = False
    tower_cell_size = params.tower_cell_size
    attack_timer = 0
    attack_cooldown = 100

    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("resource/images/Tower_Placeholder.png")
        #self.rect = pygame.Rect(0, 0, 50, 50)
        #self.rect.center = (100, 100)

    def draw(self, surface):
        #surface.blit(self.image, pygame.Rect(self.x, self.y, 50, 50))
        pygame.draw.polygon(surface, (51, 153, 51), [[self.x+self.tower_cell_size // 2, self.y],[self.x+self.tower_cell_size,self.y+self.tower_cell_size],[self.x,self.y+self.tower_cell_size]])
        #pygame.draw.rect(surface, (0,60,0), (x,y,40,40))

    def showRadius(self, surface):
        circle = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(circle, (179, 179, 179, 128), (self.radius, self.radius), self.radius) 
        surface.blit(circle, (self.x - self.radius + self.tower_cell_size // 2, self.y - self.radius + self.tower_cell_size // 2))

    def update(self, clock):
        # Обновляем таймер атаки
        self.attack_timer += clock.get_time()
        # Если прошло время атаки, вызываем метод attack() и сбрасываем таймер
        if self.attack_timer >= self.attack_cooldown:
            self.attack()
            self.attack_timer = 0

    def attack(self):
        if self.type == Type.SINGLE:
            if self.targets:
                self.targets[0].receiveDamage(self.damage)
                print('inflicted damage!')
    
    def build():
        return

    def move():
        return
    
class LMG(Tower):
    damage = 10
    radius = 150
    speed = 2
    type = Type.SINGLE
    cost = 100
    time_to_build = 10
    accuracy = 0.6
