class Player:
    def __init__(self, game):

        self.game = game
        self.stats = {
            "pulse": 180,
            "fluids": {
                1: 1,
                2: 1,
                3: 1
            },
            "rack": {
                0: False,
                1: False,
                2: False,
                3: False,
                4: False
            },
            "respiration": 1
        }
        self.death_causes = {
        }
        self.effects = {
        }

        self.current_id = 1
    
    def update(self):
        for effect in self.effects.values():
            effect.update(self)
        for death_cause in self.death_causes.values():
            if death_cause.execute(self):
                self.game.game_over(death_cause.message())

    def add_effects(self, effects):
        result = list()
        for effect in effects:
            self.current_id += 1
            result.append(self.current_id)
            self.effects[self.current_id] = effect
        return result

    def remove_effects(self, effects_ids):
        for fid in effects_ids:
            self.effects.pop(fid)

    def add_death_causes(self, dcs):
        result = list()
        for dc in dcs:
            self.current_id += 1
            result.append(self.current_id)
            self.death_causes[self.current_id] = dc
        return result

    def remove_death_causes(self, dcids):
        for dcid in dcids:
            self.death_causes.pop(dcid)

class DeathCause:
    
    def execute(self, player):
        return False

    def game_event(self, event, data):
        pass

class Effect:

    def update(self, player):
        pass

    def game_event(self, event, data):
        pass
    