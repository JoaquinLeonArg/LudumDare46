from uuid import uuid4
import logging

class Scene:

    def __init__(self, gm):
        self.gm = gm

    def update(self, dt):
        pass

    def draw(self):
        pass

    def event(self, event):
        pass