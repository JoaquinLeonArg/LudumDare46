from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg

class RackObject(WindowObject):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 300, 100)
    
    def draw(self, surface):
        super().draw(surface)
        surface.blit(ResourceManager().get_image("rack.png"), (self.x, self.y))
        for x in range(5):
            if self.window.game.player.stats["rack"][x]:
                pg.draw.rect(surface, (255, 0, 0), (x*100 + 45, self.y+15, 18, 18))
            else:
                pg.draw.rect(surface, (0, 255, 0), (x*100 + 45, self.y+15, 18, 18))
        