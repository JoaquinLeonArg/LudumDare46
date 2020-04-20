from scenes.game.windows.window import Window
from scenes.game.windows.window_objects.pills import PillsObject
from random import randrange
from resources.manager import ResourceManager

class ErrorWindow(Window):
    def __init__(self, game, message):
        super().__init__(game, "ERROR", randrange(-10, 1270), randrange(10, 700), randrange(300, 400), randrange(120, 160))
        self.message = message

    def draw(self, surface):
        super().draw(surface)
        surface.blit(ResourceManager().get_font("error").render(self.message, True, (randrange(0, 255), randrange(0, 255), randrange(0, 255))), (self.x + 16, self.y + 32))
