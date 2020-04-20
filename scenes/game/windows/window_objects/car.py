from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg
from random import choice

class CarObject(WindowObject):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 0, 0)
        self.image = choice([
            ResourceManager().get_image(f"car1.png"),
            ResourceManager().get_image(f"car2.png"),
            ResourceManager().get_image(f"car3.png")
        ])
        self.width, self.height = self.image.get_width(), self.image.get_height()
        
    def update(self):
        super().update()
        self.y += self.window.speed
        if self.y + 24 > self.window.ambulance.y and self.y < self.window.ambulance.y + 24 and abs(self.x - self.window.ambulance.x) < 10:
            self.window.game.game_over("CRASHED")
