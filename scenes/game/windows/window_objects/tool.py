from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg

class ToolObject(WindowObject):
    def __init__(self, window, x, y, image, event):
        super().__init__(window, x, y, 0, 0)
        self.image = image
        self.event = event
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)
        if self.is_inside(x, y) and mouse.is_holding(None):
            mouse.grab(self)
        