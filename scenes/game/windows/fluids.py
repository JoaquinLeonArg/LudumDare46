from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.fluid import FluidObject
from resources.manager import ResourceManager
import pygame as pg

class FluidsWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Fluids", x, y, 124, 160)
        self.objects.append(FluidObject(self, 10, 30, 1))
        self.objects.append(FluidObject(self, 50, 30, 2))
        self.objects.append(FluidObject(self, 90, 30, 3))

    def draw(self, surface):
        super().draw(surface)

    def update_mouse_pos(self, x_rel, y_rel):
        super().update_mouse_pos(x_rel, y_rel)
        if self.mouse_inside:
            self.game.info_window.notify(pg.Surface((0, 0)), "Fluids", ["Don't let any reach 0%!", "Refill by giving the", "patient some pills."])