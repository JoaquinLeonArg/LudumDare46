from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.rack import RackObject
from scenes.game.windows.window_objects.rack_button import RackButtonObject

from resources.manager import ResourceManager
import pygame as pg

class RackWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Rack", x, y, 512, 72 + 25)
        self.objects.append(RackObject(self, 0, 25))
        for x in range(5):
            self.objects.append(RackButtonObject(self, x*100 + 40, 72, x))

    def draw(self, surface):
        super().draw(surface)

    def update_mouse_pos(self, x_rel, y_rel):
        super().update_mouse_pos(x_rel, y_rel)

    def update(self):
        super().update()
        if self.mouse_inside:
            self.game.info_window.notify(pg.Surface((0, 0)), "Rack", ["Switch the lights by", "clicking the buttons.", "Don't let all lights go", "red."])