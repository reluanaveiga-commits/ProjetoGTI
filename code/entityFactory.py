#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player
from code.Obstacle import Obstacle


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:

            case 'level1Bg':

                list_bg = []

                for i in range(4):

                    list_bg.append(
                        Background(
                            f'Level1Bg{i}',
                            position
                        )
                    )

                    list_bg.append(
                        Background(
                            f'Level1Bg{i}',
                            (WIN_WIDTH, 0)
                        )
                    )

                return list_bg


            case 'level2Bg':

                list_bg = []

                for i in range(4):

                    list_bg.append(
                        Background(
                            f'Level2Bg{i}',
                            position
                        )
                    )

                    list_bg.append(
                        Background(
                            f'Level2Bg{i}',
                            (WIN_WIDTH, 0)
                        )
                    )

                return list_bg


            case 'Player1':

                return Player(
                    'Player1',
                    (
                        10,
                        WIN_HEIGHT - 100
                    )
                )


            case 'Player2':

                return Player(
                    'Player2',
                    (
                        10,
                        WIN_HEIGHT - 100
                    )
                )


            case 'Enemy1':

                return Enemy(
                    'Enemy1',
                    position if position != (0, 0)
                    else (
                        WIN_WIDTH - 100,
                        WIN_HEIGHT - 100
                    )
                )


            case 'Enemy2':

                return Enemy(
                    'Enemy2',
                    position if position != (0, 0)
                    else (
                        WIN_WIDTH - 100,
                        WIN_HEIGHT - 100
                    )
                )


            case 'Obstacle1':

                obstacle_list = [
                    'ObstacleTree',
                    'ObstacleTree1',
                    'ObstacleTree2'
                ]

                return Obstacle(
                    random.choice(obstacle_list),
                    (
                        WIN_WIDTH,
                        WIN_HEIGHT - 40
                    )
                )


        return None