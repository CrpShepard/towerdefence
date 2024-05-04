import pygame
import params

class UI(pygame.sprite.Sprite):
    width = params.screen_width
    height = params.screen_height - params.game_area_height
    surf = pygame.Surface((width, height))

    def __init__(self):
        super().__init__()
        self.grad_surf = pygame.Surface((self.width, self.height))
        for i in range(self.height):
            r = 166 + (70 - 166) * i // self.height
            g = 166 + (70 - 166) * i // self.height
            b = 166 + (70 - 166) * i // self.height
            color = (r, g, b)
            pygame.draw.line(self.grad_surf, color, (0, i), (self.width, i))

    def initUI(self):

        pass

    def drawUI(self, surface):
        surface.blit(self.grad_surf, (0, params.game_area_height))
        pass

    def updateGold(self, gold):
        pass

    def updateHealth(self, base_lives):
        pass

    def drawTowerMenu(self):
        pass

    def showDebug(self):
        pass

    def mouseHoverIn(self):
        pass

    def mouseHoverOut(self):
        pass

    def mousePressed(self):
        pass

    def mouseRelease(self):
        pass
