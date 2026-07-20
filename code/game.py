#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Score import Score
from code.level import Level
from code.menu import Menu


class Game:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode(
            size=(
                WIN_WIDTH,
                WIN_HEIGHT
            )
        )

        pygame.display.set_caption("Floresta RPG")


    def run(self):

        while True:

            # Menu
            score = Score(self.window)

            menu = Menu(self.window)

            menu_return = menu.run()



            # ===============================
            # PLAYER 1 OU PLAYER 2
            # ===============================

            if menu_return in [
                MENU_OPTION[0],
                MENU_OPTION[1]
            ]:

                player_score = [0, 0]


                # LEVEL 1
                level = Level(
                    self.window,
                    'level1',
                    menu_return,
                    player_score
                )


                level_return = level.run(player_score)



                # Jogador morreu
                if level_return is False:

                    continue



                # LEVEL 2
                if level_return:

                    level = Level(
                        self.window,
                        'level2',
                        menu_return,
                        player_score
                    )


                    level_return = level.run(player_score)



                # Jogador morreu no level 2
                if level_return is False:

                    continue



                # Final do jogo
                if level_return:

                    score.save(
                        menu_return,
                        player_score
                    )



            # ===============================
            # SCORE
            # ===============================

            elif menu_return == MENU_OPTION[2]:

                score.show()



            # ===============================
            # SAIR
            # ===============================

            elif menu_return == MENU_OPTION[3]:

                pygame.quit()
                quit()