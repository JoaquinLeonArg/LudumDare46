from scenes.scene import Scene
from resources.manager import ResourceManager
from scenes.game.windows.window import Window
from scenes.game.windows.pills import PillsWindow
from scenes.game.windows.icons import IconsWindow
from scenes.game.windows.status import *
from scenes.game.windows.info import InfoWindow
from scenes.game.windows.gadgets import GadgetsWindow
from scenes.game.windows.fluids import FluidsWindow
from scenes.game.windows.patient import PatientWindow
from scenes.game.windows.rack import RackWindow
from scenes.game.windows.road import RoadWindow
from scenes.game.windows.error_message import ErrorWindow

from scenes.game.mouse import Mouse
from scenes.game.player.player import Player
import pygame as pg
from time import strftime
import random
import sys

class SceneGame(Scene):

    def __init__(self, gm):
        super().__init__(gm)
        self.wallpaper = ResourceManager().get_image("wallpaper.png")
        self.wallpaper.blit(ResourceManager().get_image("dock.png"), (0, 720 - 53))
        self.wallpaper.blit(ResourceManager().get_image("paw.png"), (30, 720 - 52))
        self.player = Player(self)
        self.info_window = InfoWindow(self, 10, 114)
        self.status_window = StatusWindow(self, 1280 - 200 - 15, 10)
        self.pills_window = PillsWindow(self, 230, 114)
        self.icons_window = IconsWindow(self, 1080, 360)
        self.windows = [
            self.pills_window,
            self.icons_window,
            GadgetsWindow(self, 10, 10),
            FluidsWindow(self, 10, 325),
            PatientWindow(self, 576, 290),
            RackWindow(self, 10, 495),
            RoadWindow(self, 910, 440),
            self.info_window,
            self.status_window
        ]
        self.mouse = Mouse()
        self.t = 0
        self.end_game = False
        self.end_game_msg = ""

        pg.mixer.music.load("resources/music/bensound-thejazzpiano.mp3")
        pg.mixer.music.play(-1)

    def update(self, dt):
        super().update(dt)
        self.t += 1
        self.mouse.update()
        if not self.end_game:
            for window in self.windows:
                window.update()
                mouse_x, mouse_y = pg.mouse.get_pos()
                window.update_mouse_pos(mouse_x - window.x, mouse_y - window.y)
            self.player.update()
        else:
            if self.t % 5 == 0:
                self.windows.append(ErrorWindow(self, self.end_game_msg))
            if len(self.windows) > 30:
                pg.quit()
                sys.exit()

    def game_event(self, event, data=None):
        for window in self.windows:
            window.game_event(event, data)

    def game_over(self, message):
        self.end_game = True
        self.end_game_msg = message
            
    def draw(self, surface):
        surface.blit(self.wallpaper, (0, 0))
        for window in self.windows:
            window.draw(surface)
        time = ResourceManager().get_font("time").render(strftime("%H:%M"), True, (255, 255, 255))
        surface.blit(time, (1190, 682))
        self.mouse.draw(surface)
        
    def event(self, event):
        super().event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == pg.BUTTON_LEFT:
                mouse_x, mouse_y = pg.mouse.get_pos()
                for window in self.windows:
                    window.on_click(mouse_x - window.x, mouse_y - window.y, self.mouse)
            elif event.button == pg.BUTTON_RIGHT:
                self.mouse.grab(None)
        if event.type == pg.MOUSEBUTTONUP:
            mouse_x, mouse_y = pg.mouse.get_pos()
            for window in self.windows:
                window.on_release(mouse_x - window.x, mouse_y - window.y, self.mouse)