import pygame as pg
from scenes.main_menu.main_menu import SceneMainMenu
from scenes.game.game import SceneGame
from resources.constants.general import *
import sys
import cProfile

class GameWindow:
    
    def __init__(self):
        pg.init()
        self.screen_size = (1280, 720)
        self.resolution = 2
        self.window = pg.display.set_mode(self.screen_size)
        pg.mouse.set_visible(False)
        self.clock = pg.time.Clock()
        self.gm = GameManager(self)
        self.fullscreen = False
        self.loop()

    def loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_F11:
                    if self.fullscreen:
                        pg.display.set_mode(self.screen_size)
                    else:
                        pg.display.set_mode(self.screen_size, pg.FULLSCREEN)
                    self.fullscreen = not self.fullscreen
                else:
                    self.gm.event(event)
            self.gm.update(1)
            self.gm.draw(self.window)
            pg.display.flip()
            self.clock.tick(30)
            pg.display.set_caption(f'Ludum Dare 46 - {self.clock.get_fps():.0f} fps')

class GameManager:

    def __init__(self, window):
        self.window = window
        self.scene = SceneMainMenu(self)
        
    def update(self, dt):
        self.scene.update(dt)

    def draw(self, surface):
        self.scene.draw(surface)

    def event(self, event):
        self.scene.event(event)

    def change_scene(self, scene):
        self.scene = scene(self)
    
if __name__ == "__main__":
    GameWindow()