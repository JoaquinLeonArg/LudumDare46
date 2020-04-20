from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.icon import IconObject
import pygame as pg
from scenes.game import events

class IconsWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Icons", x, y, 256, 256)
        self.objects.append(IconObject(self, 0, 0, "Trash", False, None))
        self.objects.append(IconObject(self, 0, 100, "Pat", False, events.PAT))
        self.objects.append(IconObject(self, 100, 0, "Key", True, None))
    
    def draw(self, surface):
        surf = pg.Surface((256, 256), pg.SRCALPHA, 32)
        for obj in self.objects:
            obj.draw(surf)
        surface.blit(surf, (self.x, self.y))

