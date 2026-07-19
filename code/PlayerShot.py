from code.Const import ENTITY_SPEED
from code.entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple, direction=1):
        super().__init__(name, position)

        self.direction = direction


    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name] * self.direction