from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg

class FluidObject(WindowObject):
    def __init__(self, window, x, y, fluid_num):
        super().__init__(window, x, y, 24, 100)
        self.fluid_num = fluid_num
        self.color = {
            1: (100, 255, 100),
            2: (100, 0, 200),
            3: (255, 200, 200)
        }[fluid_num]
        self.perc = 1
    
    def draw(self, surface):
        super().draw(surface)
        pg.draw.rect(surface, self.color, (self.x, self.y, self.width, int(self.height*self.perc)))
        text_surf = ResourceManager().get_font("icon_name").render(f"{int(self.perc*100)}%", True, (255, 255, 255), (0, 0, 0))
        surface.blit(text_surf, (self.x + (self.width-text_surf.get_width())//2, self.y + 102))
        
    def update(self):
        super().update()
        self.perc = self.window.game.player.stats["fluids"][self.fluid_num]
