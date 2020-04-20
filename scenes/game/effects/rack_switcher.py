from scenes.game.player.player import Effect
from random import choice

class RackSwitcherEffect(Effect):

    def __init__(self, interval):
        self.interval = interval
        self.t = 0

    def update(self, player):
        self.t += 1
        if self.t % self.interval == 0:
            options = [x[0] for x in player.stats["rack"].items() if x[1] == False]
            if options:
                rack_num = choice(options)
                player.stats["rack"][rack_num] = True
        