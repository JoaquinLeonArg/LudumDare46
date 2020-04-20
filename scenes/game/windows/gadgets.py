from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.tool import ToolObject
from resources.manager import ResourceManager
from scenes.game import events
import pygame as pg

class GadgetsWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Gadgets", x, y, 600, 96)
        self.objects.append(ToolObject(self, 10, 30, ResourceManager().get_image("hammer.png"), events.HAMMER_USED))
        self.objects.append(ToolObject(self, 74, 30, ResourceManager().get_image("saw.png"), events.SAW_USED))
        self.objects.append(ToolObject(self, 138, 30, ResourceManager().get_image("pendrive.png"), events.PENDRIVE_USED))
