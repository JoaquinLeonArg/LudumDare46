from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg

class RackButtonObject(WindowObject):
    def __init__(self, window, x, y, rid):
        super().__init__(window, x, y, 0, 0)
        self.rid = rid
        self.image = ResourceManager().get_image(f"rack_button.png")
        self.width, self.height = self.image.get_width(), self.image.get_height()
    
    def draw(self, surface):
        super().draw(surface)

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)
        if self.is_inside(x, y) and mouse.is_holding(None):
            self.window.game.player.stats["rack"][self.rid] = not self.window.game.player.stats["rack"][self.rid]
