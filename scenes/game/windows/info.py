from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.status_item import StatusItemObject
from resources.manager import ResourceManager
import pygame as pg

class InfoWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Info", x, y, 200, 200)
        self.notify(pg.Surface((0, 0)), "Info window", ["Mouse over things to", "see what they do"])
    
    def notify(self, icon, title_desc, info):
        self.icon = icon
        self.title_desc = title_desc
        self.info = info
        self.title_surf = ResourceManager().get_font("status_name").render(self.title_desc, True, (255, 255, 255))

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.icon, (self.x + 6, self.y + 28))
        surface.blit(self.title_surf, (self.x + 48, self.y + 28))
        for index, line in enumerate(self.info):
            surface.blit(ResourceManager().get_font("status_desc").render(line, True, (255, 255, 255)), (self.x + 10, self.y + 64 + 15*index))

