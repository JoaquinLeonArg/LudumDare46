from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg
from random import choice

class AmbulanceObject(WindowObject):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 0, 0)
        self.image = ResourceManager().get_image("ambulance.png")
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def move(self, direction):
        if direction == "left" and self.x > 9:
            self.x -= 43
        elif direction == "right" and self.x < 95:
            self.x += 43
