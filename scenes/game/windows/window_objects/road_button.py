from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg

class RoadButtonObject(WindowObject):
    def __init__(self, window, x, y, direction):
        super().__init__(window, x, y, 0, 0)
        self.direction = direction
        self.image = ResourceManager().get_image(f"road_button_{direction}.png")
        self.width, self.height = self.image.get_width(), self.image.get_height()
    
    def draw(self, surface):
        super().draw(surface)

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)
        if self.is_inside(x, y) and mouse.is_holding(None):
            self.window.car.on_button(self.direction)
