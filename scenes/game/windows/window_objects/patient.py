from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
from scenes.game import events
import pygame as pg

class PatientObject(WindowObject):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 100, 100)
    
    def draw(self, surface):
        super().draw(surface)
        surface.blit(ResourceManager().get_image("patient.png"), (self.x, self.y))

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)
        if self.is_inside(x, y):
            if mouse.is_holding(self.window.game.pills_window.green_pill): # Green pill
                self.window.game.player.stats["fluids"][1] = min(1, self.window.game.player.stats["fluids"][1] + 0.3)
                self.window.game.game_event(events.PILL_USED)
                self.window.game.game_event(events.PILL_GREEN_USED)
                mouse.grab(None)
            if mouse.is_holding(self.window.game.pills_window.purple_pill): # Purple pill
                self.window.game.player.stats["fluids"][2] = min(1, self.window.game.player.stats["fluids"][2] + 0.3)
                mouse.grab(None)
                self.window.game.game_event(events.PILL_USED)
                self.window.game.game_event(events.PILL_PURPLE_USED)
            if mouse.is_holding(self.window.game.pills_window.pink_pill): # Pink pill
                self.window.game.player.stats["fluids"][3] = min(1, self.window.game.player.stats["fluids"][3] + 0.3)
                mouse.grab(None)
                self.window.game.game_event(events.PILL_USED)
                self.window.game.game_event(events.PILL_PINK_USED)
            try:
                if mouse.holding.event == events.PENDRIVE_USED:
                    self.window.game.game_event(events.PENDRIVE_USED)
                    mouse.grab(None)
                if mouse.holding.event == events.SAW_USED:
                    self.window.game.game_event(events.SAW_USED)
                    mouse.grab(None)
                if mouse.holding.event == events.HAMMER_USED:
                    self.window.game.game_event(events.HAMMER_USED)
                    mouse.grab(None)
            except Exception:
                pass