#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.PlayerShot import PlayerShot
from code.entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):

        super().__init__(
            name,
            position
        )

        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # Movimento RPG
        self.velocity_y = 0
        self.gravity = 1
        self.jump_force = 15
        self.on_ground = False




    def move(self):

        pressed_keys = pygame.key.get_pressed()

        speed = self.speed


        # Correr
        if pressed_keys[pygame.K_LSHIFT]:

            speed *= 2



        # Movimento horizontal
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:

            self.rect.x -= speed





        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:

            self.rect.x += speed





        # Pular
        if pressed_keys[pygame.K_SPACE] and self.on_ground:

            self.velocity_y = -self.jump_force

            self.on_ground = False



        # Gravidade
        self.velocity_y += self.gravity

        self.rect.y += self.velocity_y



        # Chão provisório
        if self.rect.bottom >= WIN_HEIGHT:

            self.rect.bottom = WIN_HEIGHT

            self.velocity_y = 0

            self.on_ground = True

    def shot(self):

        self.shot_delay -= 1

        if self.shot_delay <= 0:

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_z]:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]

                return PlayerShot(
                    name=f'{self.name}Shot',
                    position=(
                        self.rect.right - 5,
                        self.rect.top + 18
                    )
                )