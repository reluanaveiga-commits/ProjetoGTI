#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import WIN_HEIGHT, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):

        super().__init__(
            name,
            position
        )

        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # Movimento RPG
        self.velocity_y = 0
        self.gravity = 1
        self.on_ground = False



    def move(self):

        # Movimento horizontal
        self.rect.x -= self.speed


        # Gravidade
        self.velocity_y += self.gravity

        self.rect.y += self.velocity_y



        # Chão
        if self.rect.bottom >= WIN_HEIGHT:

            self.rect.bottom = WIN_HEIGHT

            self.velocity_y = 0

            self.on_ground = True



    def shot(self):

        self.shot_delay -= 1


        if self.shot_delay <= 0:

            self.shot_delay = ENTITY_SHOT_DELAY[self.name]


            return EnemyShot(
                name=f'{self.name}Shot',
                position=(
                    self.rect.centerx,
                    self.rect.centery
                )
            )