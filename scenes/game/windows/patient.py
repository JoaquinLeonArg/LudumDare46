from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.patient import PatientObject
from resources.manager import ResourceManager
import pygame as pg

class PatientWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Patient", x, y, 128, 128)
        self.objects.append(PatientObject(self, 14, 26))

    def draw(self, surface):
        super().draw(surface)

    def update_mouse_pos(self, x_rel, y_rel):
        super().update_mouse_pos(x_rel, y_rel)
        if self.mouse_inside:
            self.game.info_window.notify(pg.Surface((0, 0)), "Patient", ["Don't let him die."])

    