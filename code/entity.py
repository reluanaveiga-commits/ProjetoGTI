#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import pygame

from code.Const import (
    ENTITY_HEALTH,
    ENTITY_DAMAGE,
    ENTITY_SCORE,
    ENTITY_SPEED
)


class Entity(ABC):

    def __init__(self, name: str, position: tuple):

        self.name = name

        self.surf = pygame.image.load(
            './asset/' + name + '.png'
        ).convert_alpha()

        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )

        # Busca a velocidade definida no Const.py
        self.speed = ENTITY_SPEED[self.name]

        self.health = ENTITY_HEALTH[self.name]

        self.damage = ENTITY_DAMAGE[self.name]

        self.score = ENTITY_SCORE[self.name]

        self.last_dmg = 'None'


    @abstractmethod
    def move(self):
        pass