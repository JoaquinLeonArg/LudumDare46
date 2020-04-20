import pygame as pg

class WindowObject:
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.image = pg.Surface((0, 0))
        self.mouse_inside = False
        self.needs_redraw = False

    def update(self):
        pass

    def update_mouse_pos(self, x_rel, y_rel):
        if self.is_inside(x_rel, y_rel):
            self.mouse_inside = True
        else:
            self.mouse_inside = False

    def on_click(self, x, y, mouse):
        pass
    
    def on_release(self, x, y, mouse):
        pass

    def game_event(self, event, data):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def is_inside(self, x, y):
        return x > 0 and x < self.width and y > 0 and y < self.height