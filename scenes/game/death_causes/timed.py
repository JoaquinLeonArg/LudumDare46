from scenes.game.player.player import DeathCause
from scenes.game import events

class TimedDeathCause(DeathCause):

    def __init__(self, time):
        self.time = time
    
    def execute(self, player):
        self.time -= 1
        if self.time == 0:
            return True
        return False

    def message(self):
        return "PAT ME HUMAN"