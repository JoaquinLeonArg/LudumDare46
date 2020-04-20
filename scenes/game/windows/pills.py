from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.pills import PillsObject
from resources.manager import ResourceManager

import pygame as pg

class PillsWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Pills", x, y, 160, 120)
        self.green_pill = (PillsObject(self, 15, 45, "green"))
        self.objects.append(self.green_pill)
        self.purple_pill = (PillsObject(self, 65, 45, "purple"))
        self.objects.append(self.purple_pill)
        self.pink_pill = (PillsObject(self, 115, 45, "pink"))
        self.objects.append(self.pink_pill)
        self.locked = True
    
    def draw(self, surface):
        super().draw(surface)
        if self.locked:
            surface.blit(ResourceManager().get_image("lock.png"), (self.x+1, self.y + 25))

    def on_click(self, mouse_x, mouse_y, mouse):
        if not self.is_inside(mouse_x, mouse_y):
            return
        if self.locked:
            if mouse.is_holding(self.game.icons_window.objects[2]): # Key
                mouse.grab(None)
                self.locked = False
            return
        super().on_click(mouse_x, mouse_y, mouse)

    def update_mouse_pos(self, x_rel, y_rel):
        super().update_mouse_pos(x_rel, y_rel)
        if self.mouse_inside and self.locked:
            self.game.info_window.notify(pg.Surface((0, 0)), "Pills", ["Unlock with the key."])
