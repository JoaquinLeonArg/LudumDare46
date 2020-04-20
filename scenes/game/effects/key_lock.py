from scenes.game.player.player import Effect
from random import randrange

class KeyLockEffect(Effect):

    def __init__(self):
        self.t = 0

    def update(self, player):
        self.t += 1
        if randrange(500, 1000) < self.t:
            self.t = 0
            player.game.pills_window.locked = True
            