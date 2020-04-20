from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.status_item import StatusItemObject
from scenes.game.effects.fluid_decreaser import FluidDecreaserEffect
from scenes.game.effects.rack_switcher import RackSwitcherEffect
from scenes.game.effects.key_lock import KeyLockEffect
from scenes.game.death_causes.rack_off import RackOffDeathCause
from scenes.game.death_causes.fluid_empty import FluidLowDeathCause
from scenes.game.death_causes.timed import TimedDeathCause
from scenes.game import events
from resources.manager import ResourceManager

import pygame as pg
from random import choice

class StatusWindow(Window):

    def __init__(self, game, x, y):
        super().__init__(game, "Status", x, y, 200, 326)
        self.difficulty = 1
        self.game.player.add_effects([
            FluidDecreaserEffect(1, 0.0005),
            FluidDecreaserEffect(2, 0.0005),
            FluidDecreaserEffect(3, 0.0005)
            ])
        self.game.player.add_death_causes([
            FluidLowDeathCause(0.01),
            RackOffDeathCause()
        ])


    def add_status(self, status_class):
        if len(self.objects) < 6:
            self.objects.append(status_class(self, 2, len(self.objects)*50 + 26, self.difficulty))
    
    def update(self):
        super().update()
        if self.t % max(100, 400-self.difficulty*20) == 0:
            self.difficulty += 1
            self.add_status(choice([
                Fluiditis,
                Nopatitis,
                Trojan,
                Fedoravirus,
                Keylocker,
                DDoS
            ]))

    def remove_object(self, obj):
        super().remove_object(obj)
        for index, o in enumerate(self.objects):
            o.y = index*50 + 26

class Fluiditis(StatusItemObject):
    def __init__(self, window, x, y, difficulty):
        effects = [
            FluidDecreaserEffect(choice([1, 2, 3]), choice([0.0001, 0.00015]))
        ]
        super().__init__(window, x, y, effects, [], "Fluiditis", ["Slowly drains your fluids", "over time."], ResourceManager().get_image("fluiditis.png"), difficulty)
    def update(self):
        super().update()
        if self.t > 1000:
            self.window.game.player.remove_effects(self.effects_ids)
            self.window.remove_object(self)
    def draw(self, surface):
        super().draw(surface)
        draw_bar(surface, self.x + 45, self.y + 30, max(0, ((1000)-self.t)/(1000)), (0, 255, 0))

class Nopatitis(StatusItemObject):
    def __init__(self, window, x, y, difficulty):
        dcs = [TimedDeathCause(10 * 60)]
        super().__init__(window, x, y, [], dcs, "Nopatitis", ["Kills the patient if you", "don't pat him."], ResourceManager().get_image("nopatitis.png"), difficulty)
    def game_event(self, event, data):
        if event == events.PAT:
            self.window.game.player.remove_death_causes(self.death_causes_ids)
            self.window.game.player.remove_effects(self.effects_ids)
            self.window.remove_object(self)
    def draw(self, surface):
        super().draw(surface)
        draw_bar(surface, self.x + 45, self.y + 30, max(0, ((10*60)-self.t)/(10*60)), (255, 0, 0))

class Fedoravirus(StatusItemObject):
    def __init__(self, window, x, y, difficulty):
        self.max_time = max(250, 600-difficulty*50)
        dcs = [TimedDeathCause(self.max_time)]
        super().__init__(window, x, y, [], dcs, "Fedoravirus", ["Kills the patient if you", "don't use the saw on him."], ResourceManager().get_image("fedora.png"), difficulty)
    def game_event(self, event, data):
        if event == events.SAW_USED:
            self.window.game.player.remove_death_causes(self.death_causes_ids)
            self.window.game.player.remove_effects(self.effects_ids)
            self.window.remove_object(self)
    def draw(self, surface):
        super().draw(surface)
        draw_bar(surface, self.x + 45, self.y + 30, max(0, (self.max_time-self.t)/self.max_time), (255, 0, 0))

class Trojan(StatusItemObject):
    def __init__(self, window, x, y, difficulty):
        self.max_time = max(250, 600-difficulty*50)
        dcs = [TimedDeathCause(self.max_time)]
        super().__init__(window, x, y, [], dcs, "Trojan", ["Kills the patient if you", "don't use the pendrive", "on him."], ResourceManager().get_image("trojan.png"), difficulty)
    def game_event(self, event, data):
        if event == events.PENDRIVE_USED:
            self.window.game.player.remove_death_causes(self.death_causes_ids)
            self.window.game.player.remove_effects(self.effects_ids)
            self.window.remove_object(self)
    def draw(self, surface):
        super().draw(surface)
        draw_bar(surface, self.x + 45, self.y + 30, max(0, (self.max_time-self.t)/self.max_time), (255, 0, 0))

class DDoS(StatusItemObject):
    def __init__(self, window, x, y, difficulty):
        self.time_between = max(30, 120-difficulty*30)
        effects = [RackSwitcherEffect(100)]
        super().__init__(window, x, y, effects, [], "DDoS", ["Turns off your rack ports", "Disable it by using the", "hammer."], ResourceManager().get_image("ddos.png"), difficulty)
    def game_event(self, event, data):
        if event == events.HAMMER_USED:
            self.window.game.player.remove_death_causes(self.death_causes_ids)
            self.window.game.player.remove_effects(self.effects_ids)
            self.window.remove_object(self)
    def update(self):
        super().update()
        if self.t > 10000:
            self.window.game.player.remove_effects(self.effects_ids)
            self.window.remove_object(self)
    def draw(self, surface):
        super().draw(surface)
        draw_bar(surface, self.x + 45, self.y + 30, max(0, ((10000)-self.t)/(10000)), (0, 255, 0))

class Keylocker(StatusItemObject):
    def __init__(self, window, x, y, difficulty):
        effects = [KeyLockEffect()]
        super().__init__(window, x, y, effects, [], "Keylocker", ["Randomly locks your pills."], ResourceManager().get_image("keylogger.png"), difficulty)
    def update(self):
        super().update()
        if self.t > 1000:
            self.window.game.player.remove_effects(self.effects_ids)
            self.window.remove_object(self)
    def draw(self, surface):
        super().draw(surface)
        draw_bar(surface, self.x + 45, self.y + 30, max(0, ((1000)-self.t)/(1000)), (0, 255, 0))

def draw_bar(surface, x, y, perc, color):
    pg.draw.rect(surface, (100, 100, 100), (x, y, 140, 12))
    pg.draw.rect(surface, color, (x, y, 140*perc, 12))