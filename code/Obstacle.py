#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Obstacle(Entity):

    def __init__(self, name: str, position: tuple):

        super().__init__(
            name,
            position
        )



    def move(self):

        self.rect.x -= self.speed

        if self.rect.right < 0:

            self.health = 0