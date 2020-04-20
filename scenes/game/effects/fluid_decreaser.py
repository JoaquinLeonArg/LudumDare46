from scenes.game.player.player import Effect

class FluidDecreaserEffect(Effect):

    def __init__(self, fluid_num, rate):
        self.fluid_num = fluid_num
        self.rate = rate

    def update(self, player):
        player.stats["fluids"][self.fluid_num] = max(0, player.stats["fluids"][self.fluid_num]-self.rate)
        