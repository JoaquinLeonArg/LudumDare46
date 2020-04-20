import pygame as pg
from resources.manager import ResourceManager

class Window:

    def __init__(self, game, title, x, y, width, height):
        self.game = game
        self.title = title
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.render_opacity = 255
        self.mouse_inside = False
        self.objects = list()
        self.t = 0

    def update(self):
        if self.mouse_inside:
            self.render_opacity = 255
        else:
            self.render_opacity = 230
        for obj in self.objects:
            obj.update()
        self.t += 1

    def update_mouse_pos(self, x_rel, y_rel):
        if self.is_inside(x_rel, y_rel):
            self.mouse_inside = True
        else:
            self.mouse_inside = False
        for obj in self.objects:
            obj.update_mouse_pos(x_rel - obj.x, y_rel - obj.y)

    def on_click(self, x_rel, y_rel, mouse):
        if not self.is_inside(x_rel, y_rel):
            return
        for obj in self.objects:
            obj.on_click(x_rel - obj.x, y_rel - obj.y, mouse)

    def game_event(self, event, data=None):
        for obj in self.objects:
            obj.game_event(event, data=None)
    
    def on_release(self, x_rel, y_rel, mouse):
        if not self.is_inside(x_rel, y_rel):
            return
        for obj in self.objects:
            obj.on_release(x_rel - obj.x, y_rel - obj.y, mouse)

    def draw(self, surface):
        surface.fill((10, 10, 10), (self.x + 8, self.y + 4, self.width, self.height))
        surf = pg.Surface((self.width, self.height))
        surf.set_alpha(self.render_opacity)
        surf.blit(ResourceManager().get_image("window_title.png"), (0, 0))
        surf.blit(ResourceManager().get_image("window_bg.png"), (0, 25))
        pg.draw.rect(surf, (200, 200, 255), (0, 0, self.width, self.height), width=2)
        title_text = ResourceManager().get_font("window_title").render(self.title, True, (255, 255, 255))
        surf.blit(title_text, (8, 4))
        for obj in self.objects:
            obj.draw(surf)
        surface.blit(surf, (self.x, self.y))

    def is_inside(self, x, y):
        return x > 0 and x < self.width and y > 0 and y < self.height

    def remove_object(self, obj):
        self.objects.remove(obj)
