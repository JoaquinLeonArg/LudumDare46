from scenes.game.player.player import DeathCause

class FluidLowDeathCause(DeathCause):

    def __init__(self, threshold):
        self.threshold = threshold
    
    def execute(self, player):
        return player.stats["fluids"][1] < self.threshold or player.stats["fluids"][2] < self.threshold or player.stats["fluids"][3] < self.threshold

    def message(self):
        return "FLUIDS TOO LOW"