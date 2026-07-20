#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    C_WHITE,
    C_GREEN,
    TIMEOUT_LEVEL,
    SPAWM_TIME,
    OBSTACLE_TIME,
    C_RED,
    C_GOLD,
    C_BLACK
)

from code.EntityMediator import EntityMediator
from code.entityFactory import EntityFactory
from code.entity import Entity
from code.player import Player
from code.enemy import Enemy
from code.Obstacle import Obstacle


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):

        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []

        # Controle de spawn
        self.enemy_spawn = 1

        # Controle de obstáculos
        self.obstacle_timer = pygame.time.get_ticks()

        # Tempo da fase
        self.start_time = pygame.time.get_ticks()

        # ==========================
        # Música da fase
        # ==========================
        pygame.mixer.music.stop()

        if self.name.lower() == 'level1':
            pygame.mixer.music.load('./asset/Level1.mp3')

        elif self.name.lower() == 'level2':
            pygame.mixer.music.load('./asset/Level2.mp3')

        pygame.mixer.music.play(-1)

        # Fundo
        self.entity_list.extend(
            EntityFactory.get_entity(self.name + 'Bg')
        )

        # Jogador escolhido no menu
        if self.game_mode == 'PLAYER 1':
            player = EntityFactory.get_entity('Player1')

        elif self.game_mode == 'PLAYER 2':
            player = EntityFactory.get_entity('Player2')

        else:
            player = EntityFactory.get_entity('Player1')

        player.score = player_score[0]

        self.entity_list.append(player)

        # Primeiro inimigo
        self.entity_list.append(
            EntityFactory.get_entity(
                'Enemy1',
                (
                    WIN_WIDTH,
                    WIN_HEIGHT - 80
                )
            )
        )


    def run(self, player_score: list[int]):

        clock = pygame.time.Clock()

        # Spawn inimigos a cada 3 segundos
        pygame.time.set_timer(
            pygame.USEREVENT + 10,
            SPAWM_TIME
        )


        while True:

            clock.tick(60)


            # Eventos
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                # Spawn de inimigos
                if event.type == pygame.USEREVENT + 10:


                    if self.enemy_spawn == 1:

                        self.entity_list.append(
                            EntityFactory.get_entity(
                                'Enemy1',
                                (
                                    WIN_WIDTH,
                                    WIN_HEIGHT - 80
                                )
                            )
                        )

                        self.enemy_spawn = 2


                    else:

                        self.entity_list.append(
                            EntityFactory.get_entity(
                                'Enemy2',
                                (
                                    WIN_WIDTH,
                                    WIN_HEIGHT - 80
                                )
                            )
                        )

                        self.enemy_spawn = 1



            # ===============================
            # Spawn dos obstáculos
            # ===============================

            current_time = pygame.time.get_ticks()


            if current_time - self.obstacle_timer >= OBSTACLE_TIME:


                self.entity_list.append(
                    EntityFactory.get_entity(
                        'Obstacle1',
                        (
                            WIN_WIDTH,
                            WIN_HEIGHT - 80
                        )
                    )
                )


                self.obstacle_timer = current_time



            # Atualiza entidades
            for ent in self.entity_list[:]:


                self.window.blit(
                    source=ent.surf,
                    dest=ent.rect
                )


                ent.move()



                # Tiro
                if isinstance(ent, (Player, Enemy)):


                    shot = ent.shot()


                    if shot is not None:

                        self.entity_list.append(shot)



                # Vida jogador
                if isinstance(ent, Player):

                    self.level_text(
                        text_size=18,
                        text=f'Vida: {ent.health}  Pontos: {ent.score}',
                        text_color=C_GOLD,
                        text_pos=(10, 10)
                    )



            # Colisão
            EntityMediator.verify_collision(
                entity_list=self.entity_list
            )


            EntityMediator.verify_health(
                entity_list=self.entity_list
            )



            # Verifica se jogador morreu
            player_alive = any(
                isinstance(ent, Player)
                for ent in self.entity_list
            )


            if not player_alive:


                pygame.time.set_timer(
                    pygame.USEREVENT + 10,
                    0
                )


                return False



            # Atualiza score
            for ent in self.entity_list:


                if isinstance(ent, Player):

                    player_score[0] = ent.score




            # Tempo da fase
            elapsed_time = pygame.time.get_ticks() - self.start_time


            remaining_time = max(
                0,
                (TIMEOUT_LEVEL - elapsed_time) // 1000
            )



            self.level_text(
                text_size=14,
                text=f'Tempo: {remaining_time}',
                text_color=C_WHITE,
                text_pos=(WIN_WIDTH - 100, 10)
            )



            # Final da fase pelo tempo
            if elapsed_time >= TIMEOUT_LEVEL:


                pygame.time.set_timer(
                    pygame.USEREVENT + 10,
                    0
                )


                return True



            # FPS
            self.level_text(
                text_size=14,
                text=f'FPS: {clock.get_fps():.0f}',
                text_color=C_GREEN,
                text_pos=(10, WIN_HEIGHT - 30)
            )



            pygame.display.flip()



    def level_text(
            self,
            text_size: int,
            text: str,
            text_color: tuple,
            text_pos: tuple):


        text_font: Font = pygame.font.SysFont(
            'Arial',
            text_size,
            bold=True
        )


        # Sombra
        shadow_surf: Surface = text_font.render(
            text,
            True,
            C_BLACK
        ).convert_alpha()


        shadow_rect: Rect = shadow_surf.get_rect(
            left=text_pos[0] + 2,
            top=text_pos[1] + 2
        )


        self.window.blit(
            source=shadow_surf,
            dest=shadow_rect
        )



        # Texto principal
        text_surf: Surface = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()


        text_rect: Rect = text_surf.get_rect(
            left=text_pos[0],
            top=text_pos[1]
        )


        self.window.blit(
            source=text_surf,
            dest=text_rect
        )