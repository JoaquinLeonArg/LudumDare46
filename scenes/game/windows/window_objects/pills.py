from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg

class PillsObject(WindowObject):
    def __init__(self, window, x, y, color):
        super().__init__(window, x, y, 0, 0)
        self.color = color
        self.image = ResourceManager().get_image(f"pills_{self.color}.png")
        self.width, self.height = self.image.get_width(), self.image.get_height()
    
    def draw(self, surface):
        super().draw(surface)

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)
        if self.is_inside(x, y) and mouse.is_holding(None):
            mouse.grab(self)

    def update_mouse_pos(self, x_rel, y_rel):
        super().update_mouse_pos(x_rel, y_rel)
        if self.mouse_inside and not self.window.locked:
            color = {
                "pink": "Pink",
                "green": "Green",
                "purple": "Purple"
            }
            self.window.game.info_window.notify(pg.Surface((0, 0)), f"{color[self.color]} pills", ["Refills some fluids.", "Give them to the patient."])
