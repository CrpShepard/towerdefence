import pygame
import params

class UI(pygame.sprite.Sprite):
    width = params.screen_width
    height = params.screen_height - params.game_area_height
    margin = 10
    surf = pygame.Surface((width, height))
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)

    def __init__(self):
        super().__init__()
        self.gradBackground()
        self.drawTowerMenu()
        self.drawStatsArea()
        self.drawButtonsArea()

    def gradBackground(self):
        self.surf = pygame.Surface((self.width, self.height))
        for i in range(self.height):
            r = 166 + (70 - 166) * i // self.height
            g = 166 + (70 - 166) * i // self.height
            b = 166 + (70 - 166) * i // self.height
            color = (r, g, b)
            pygame.draw.line(self.surf, color, (0, i), (self.width, i))

    def drawUI(self, surface):
        self.surf.blit(self.surf_statsArea, (self.width * 2/3 + self.margin * 2, self.margin))
        surface.blit(self.surf, (0, params.game_area_height))
        pass

    def drawStatsArea(self):
        self.surf_statsArea = pygame.Surface((self.width * 1/6, self.height - self.margin * 2))
        pygame.draw.rect(self.surf_statsArea, (120, 120, 120), (0, 0, self.width * 1/6, self.height - self.margin * 2))
        #self.surf.blit(self.surf_statsArea, (self.width * 2/3 + self.margin * 2, self.margin))

    def updateGold(self, gold):
        text_surface = self.my_font.render("Gold: " + str(gold), False, (0, 0, 0))
        subSurf = pygame.Surface((text_surface.get_width(), text_surface.get_height()))
        pygame.draw.rect(subSurf, (120, 120, 120), (0, 0, text_surface.get_width(), text_surface.get_height()))
        subSurf.blit(text_surface, (0, 0))
        self.surf_statsArea.blit(subSurf, (5, 30))

    def updateHealth(self, base_lives):
        text_surface = self.my_font.render("Base lives: " + str(base_lives), False, (0, 0, 0))
        subSurf = pygame.Surface((text_surface.get_width(), text_surface.get_height()))
        pygame.draw.rect(subSurf, (120, 120, 120), (0, 0, text_surface.get_width(), text_surface.get_height()))
        subSurf.blit(text_surface, (0, 0))
        self.surf_statsArea.blit(subSurf, (5, 5))

    def drawTowerMenu(self):
        self.surf_towerMenu = pygame.Surface((self.width * 2/3, self.height - self.margin * 2))
        pygame.draw.rect(self.surf_towerMenu, (120, 120, 120), (0, 0, self.width * 2/3, self.height - self.margin * 2))
        self.surf.blit(self.surf_towerMenu, (self.margin, self.margin))
        pass

    def drawButtonsArea(self):
        self.surf_buttonsArea = pygame.Surface((self.width * 1/6 - self.margin * 4, self.height - self.margin * 2))
        pygame.draw.rect(self.surf_buttonsArea, (120, 120, 120), (0, 0, self.width * 1/6 - self.margin, self.height - self.margin * 2))
        self.surf.blit(self.surf_buttonsArea, (self.width * 2/3 + self.width * 1/6 + self.margin * 3, self.margin))

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
