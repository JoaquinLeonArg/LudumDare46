from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg
from copy import copy

class IconObject(WindowObject):
    def __init__(self, window, x, y, icon_name, grabable, event_on_click):
        super().__init__(window, x, y, 0, 0)
        self.icon_name = icon_name
        self.grabable = grabable
        self.event_on_click = event_on_click
        self.image = ResourceManager().get_image(f"icon_{self.icon_name}.png")
        self.dark_image = copy(ResourceManager().get_image(f"icon_{self.icon_name}.png"))
        dark = pg.Surface((self.dark_image.get_width(), self.dark_image.get_height()), flags=pg.SRCALPHA)
        dark.fill((200, 200, 200, 0))
        self.dark_image.blit(dark, (0, 0), special_flags=pg.BLEND_RGBA_SUB)
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.text_surf = ResourceManager().get_font("icon_name").render(self.icon_name, True, (255, 255, 255), (0, 0, 0))
    
    def draw(self, surface):
        surface.blit(self.dark_image, (self.x + 8, self.y + 4))
        surface.blit(self.text_surf, (self.x + (72 - self.text_surf.get_width())//2, self.y + 80))
        super().draw(surface)

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)
        if self.event_on_click and self.is_inside(x, y) and mouse.is_holding(None):
            self.window.game.game_event(self.event_on_click)
        if self.is_inside(x, y) and self.grabable and mouse.is_holding(None):
            mouse.grab(self)
