from scenes.game.player.player import DeathCause

class RackOffDeathCause(DeathCause):
    
    def execute(self, player):
        return all([x for x in player.stats["rack"].values()])

    def message(self):
        return "RACK OFFLINE"