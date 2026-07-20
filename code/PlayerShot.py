from code.Const import ENTITY_SPEED
from code.entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Centraliza o tiro na posição recebida
        self.rect.center = position

    def move(self):
        # Sempre move para a direita
        self.rect.x += ENTITY_SPEED[self.name]