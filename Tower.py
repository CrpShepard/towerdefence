import pygame

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
    focus = 0
    focus_group = []
    engage = False

    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("resource/images/Tower_Placeholder.png")
        #self.rect = pygame.Rect(0, 0, 50, 50)
        #self.rect.center = (100, 100)

    def draw(self, surface):
        #surface.blit(self.image, pygame.Rect(self.x, self.y, 50, 50))
        pygame.draw.polygon(surface, (51, 153, 51), [[self.x+20, self.y],[self.x+40,self.y+40],[self.x,self.y+40]])
        #pygame.draw.rect(surface, (0,60,0), (x,y,40,40))

    def showRadius(self, surface):
        circle = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(circle, (179, 179, 179, 128), (self.radius, self.radius), self.radius) 
        surface.blit(circle, (self.x - self.radius + 20, self.y - self.radius + 20))

    def attack(self):
        if self.type == 0:
            pass
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
    type = 0
    cost = 100
    time_to_build = 10
    accuracy = 0.6
