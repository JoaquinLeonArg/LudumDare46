from resources.manager import ResourceManager
import pygame as pg

class Mouse:
    def __init__(self):
        self.holding = None
        self.default_image = ResourceManager().get_image("mouse_default.png")
        self.x, self.y = 0, 0

    def grab(self, obj):
        self.holding = obj
    
    def is_holding(self, obj):
        return self.holding == obj

    def draw(self, surface):
        if self.holding:
            surface.blit(self.holding.image, (self.x, self.y))
        else:
            surface.blit(self.default_image, (self.x, self.y))

    def update(self):
        self.x, self.y = pg.mouse.get_pos()