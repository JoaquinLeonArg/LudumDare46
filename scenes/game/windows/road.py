from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.car import CarObject
from scenes.game.windows.window_objects.ambulance import AmbulanceObject
from scenes.game.windows.window_objects.window_object import WindowObject

from resources.manager import ResourceManager
import pygame as pg
from random import choice

class RoadWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Road", x, y, 127, 210)
        self.speed = 0.2
        self.ambulance = AmbulanceObject(self, 54, 130)
        self.objects.append(self.ambulance)
        self.objects.append(RoadButton(self, 4, 188, "left"))
        self.objects.append(RoadButton(self, 96, 188, "right"))
        self.cars = list()
        self.difficulty = 1

    def draw(self, surface):
        surf = pg.Surface((124, 160))
        surf.blit(ResourceManager().get_image("road.png"), (0, (self.t*self.speed)%160))
        surf.blit(ResourceManager().get_image("road.png"), (0, (self.t*self.speed)%160 - 160))
        for car in self.cars:
            car.draw(surf)
        self.ambulance.draw(surf)
        super().draw(surface)
        surface.blit(surf, (self.x + 2, self.y + 25))
        
    def update(self):
        super().update()
        self.speed = self.difficulty/5
        for car in self.cars:
            car.update()
        if self.t % max(180, 600-self.difficulty*50) == 0:
            self.cars.append(CarObject(self, choice([9, 54, 97]), -10))

    def update_mouse_pos(self, x_rel, y_rel):
        super().update_mouse_pos(x_rel, y_rel)
        if self.mouse_inside:
            self.game.info_window.notify(pg.Surface((0, 0)), "Road", ["Don't let the ambulance", "crash into a car."])

class RoadButton(WindowObject):

    def __init__(self, window, x, y, direction):
        self.direction = direction
        super().__init__(window, x, y, 0, 0)
        self.image = ResourceManager().get_image(f"{self.direction}_button.png")
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def draw(self, surface):
        super().draw(surface)

    def on_click(self, x, y, mouse):
        super().on_click(x, y, mouse)
        if self.is_inside(x, y) and mouse.is_holding(None):
            self.window.ambulance.move(self.direction)