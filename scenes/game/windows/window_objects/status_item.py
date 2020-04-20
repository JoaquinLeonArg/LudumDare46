from scenes.game.windows.window_objects.window_object import WindowObject
from resources.manager import ResourceManager
import pygame as pg

class StatusItemObject(WindowObject):
    def __init__(self, window, x, y, effects, dcs, name, description, icon, difficulty):
        super().__init__(window, x, y, 0, 0)
        self.name = name
        self.description = description
        self.icon = icon
        self.effects_ids = self.window.game.player.add_effects(effects)
        self.death_causes_ids = self.window.game.player.add_death_causes(dcs)
        self.difficulty = difficulty
        self.image = pg.Surface((self.window.width - 4, 48))
        self.image.fill((0, 0, 50))
        pg.draw.rect(self.image, (255, 255, 255), (0, 0, self.window.width - 5, 47), width=2)
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.name_surf = ResourceManager().get_font("status_name").render(self.name, True, (255, 255, 255))
        self.t = 0
    
    def draw(self, surface):
        if self.mouse_inside:
            self.image.fill((0, 0, 120))
        else:
            self.image.fill((0, 0, 50))
        pg.draw.rect(self.image, (255, 255, 255), (0, 0, self.window.width - 5, 47), width=2)
        self.image.blit(self.icon, (3, 6))
        self.image.blit(self.name_surf, (48, 6))
        super().draw(surface)

    def update(self):
        super().update()
        self.t += 1

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)

    def update_mouse_pos(self, x_rel, y_rel):
        super().update_mouse_pos(x_rel, y_rel)
        if self.mouse_inside:
            self.window.game.info_window.notify(self.icon, self.name, self.description)
    
    def on_destroy(self):
        self.window.game.player.remove_effects(self.effects_ids)
