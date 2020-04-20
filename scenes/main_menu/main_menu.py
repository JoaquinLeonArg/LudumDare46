from scenes.scene import Scene
from scenes.game.game import SceneGame
from resources.manager import ResourceManager
import pygame as pg
from random import randrange
from resources.constants.menu import *
import sys

class SceneMainMenu(Scene):

    def __init__(self, gm):
        super().__init__(gm)
        self.font = ResourceManager().get_font("menu_large")
        self.buttons = [
            Button(80, 620, ResourceManager().get_image("quit.png"), ResourceManager().get_image("quit_active.png"), sys.exit),
            Button(680, 260, ResourceManager().get_image("start.png"), ResourceManager().get_image("start_active.png"), lambda: self.gm.change_scene(SceneGame))
        ]

    def update(self, dt):
        super().update(dt)
        for button in self.buttons:
            button.update_mouse_position(*pg.mouse.get_pos())

    def draw(self, surface):
        surface.blit(ResourceManager().get_image("menu_bg.png"), (0, 0))
        surface.blit(ResourceManager().get_image("logo.png"), (100, 220))
        for button in self.buttons:
            button.draw(surface)
        surface.blit(ResourceManager().get_font("menu_large").render("Start game", True, (255, 255, 255)), (850, 290))
        surface.blit(ResourceManager().get_image("mouse_default.png"), pg.mouse.get_pos())

    def event(self, event):
        super().event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == pg.BUTTON_LEFT:
                for button in self.buttons:
                    button.on_click()

class Button:

    def __init__(self, x, y, image_inactive, image_active, action):
        self.x, self.y = x, y
        self.width = image_active.get_width()
        self.height = image_active.get_height()
        self.image_inactive = image_inactive
        self.image_active = image_active
        self.action = action
        self.image = image_inactive
        self.active = False

    def update_mouse_position(self, mouse_x, mouse_y):
        if mouse_x > self.x and mouse_x < self.x + self.width and mouse_y > self.y and mouse_y < self.y + self.height:
            self.image = self.image_active
            self.active = True
        else:
            self.image = self.image_inactive
            self.active = False

    def on_click(self):
        if self.active:
            self.action()
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
