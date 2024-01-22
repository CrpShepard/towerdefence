import pygame

class Tower(pygame.sprite.Sprite):
    damage = 0
    radius = 0
    speed = 0
    effect = []
    type = "placeholder"
    cost = 0
    time_to_build = 0
    current_coords = [0, 0]
    accuracy = 0
    focus = 0
    focus_group = []
    engage = False

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resource/images/Tower_Placeholder.png")
        #self.rect = pygame.Rect(0, 0, 50, 50)
        #self.rect.center = (100, 100)

    def draw(self, surface):
        surface.blit(self.image, pygame.Rect(self.current_coords[0], self.current_coords[1], 50, 50))

    def attack():
        return
    
    def build():
        return

    def move():
        return
    
    def isEnemy():
        return
    
class LMG(Tower):
    damage = 5
    radius = 300
    speed = 2
    type = "machine_gun"
    cost = 100
    time_to_build = 10
    accuracy = 0.6
