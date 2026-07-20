#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

# ===========================
# CORES
# ===========================

# Cores básicas
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)

# Interface (HUD)
C_RED = (220, 40, 40)  # Vida
C_GOLD = (255, 215, 0)  # Pontuação
C_GREEN = (0, 220, 0)  # FPS
C_CYAN = (0, 220, 220)  # Informações
C_YELLOW = (255, 255, 0)  # Destaques
C_ORANGE = (255, 140, 0)  # Títulos

# Sombra do texto
C_SHADOW = (30, 30, 30)

# ===========================
# EVENTOS
# ===========================

EVENT_TIMEOUT = pygame.USEREVENT + 1
EVENT_ENEMY = pygame.USEREVENT + 2

# ===========================
# VELOCIDADE DAS ENTIDADES
# ===========================

ENTITY_SPEED = {

    # Cenários
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,

    'Level2Bg0': 1,
    'Level2Bg1': 1,
    'Level2Bg2': 1,
    'Level2Bg3': 1,

    # Jogador
    'Player1': 5,
    'Player2': 5,

    # Tiros
    'Player1Shot': 8,
    'Player2Shot': 8,

    # Inimigos
    'Enemy1': 2,
    'Enemy2': 2,

    # Tiros inimigos
    'Enemy1Shot': 5,
    'Enemy2Shot': 5,

    'ObstacleTree': 1,
    'ObstacleTree1': 1,
    'ObstacleTree2': 1,
}

# ===========================
# DANO
# ===========================


ENTITY_DAMAGE = {

    # Cenário
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,

    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,

    # Jogador
    'Player1': 10,
    'Player2': 10,

    # Tiros
    'Player1Shot': 25,
    'Player2Shot': 25,

    # Inimigos
    'Enemy1': 15,
    'Enemy2': 20,

    # Tiros inimigos
    'Enemy1Shot': 10,
    'Enemy2Shot': 15,

    # Obstáculos
    'ObstacleTree': 25,
    'ObstacleTree1': 25,
    'ObstacleTree2': 25,
}

# ===========================
# OBSTACULO
# ===========================

OBSTACLE_DELAY = 3000
OBSTACLE_TIME = 10000

# ===========================
# TEMPO ENTRE ATAQUES
# ===========================

ENTITY_SHOT_DELAY = {

    'Player1': 20,
    'Player2': 20,

    'Enemy1': 100,
    'Enemy2': 120,
}

# ===========================
# VIDA
# ===========================

ENTITY_HEALTH = {

    # Cenário
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,

    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,

    # Jogador
    'Player1': 100,
    'Player2': 100,

    # Tiros
    'Player1Shot': 1,
    'Player2Shot': 1,

    # Inimigos
    'Enemy1': 50,
    'Enemy2': 70,

    # Tiros inimigos
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,

    # Obstáculos
    'ObstacleTree': 1,
    'ObstacleTree1': 1,
    'ObstacleTree2': 1,
}

# ===========================
# MENU
# ===========================

MENU_OPTION = (
    'PLAYER 1',
    'PLAYER 2',
    'PONTUAÇÃO',
    'EXIT'
)

# ===========================
# CONTROLES
# ===========================

PLAYER_KEY_LEFT = {

    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a,

}

PLAYER_KEY_RIGHT = {

    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d,

}

PLAYER_KEY_SHOT = {

    'Player1': pygame.K_z,
    'Player2': pygame.K_LCTRL,

}

# ===========================
# PONTUAÇÃO
# ===========================

ENTITY_SCORE = {

    # Cenários
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,

    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,

    # Jogador
    'Player1': 0,
    'Player2': 0,

    # Tiros
    'Player1Shot': 0,
    'Player2Shot': 0,

    # Inimigos
    'Enemy1': 100,
    'Enemy2': 150,

    # Tiros inimigos
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,

    # Obstáculos
    'ObstacleTree': 0,
    'ObstacleTree1': 0,
    'ObstacleTree2': 0,
}

# ===========================
# SPAWN / TEMPO
# ===========================

SPAWM_TIME = 3000

TIMEOUT_LEVEL = 30000

TIMEOUT_STEP = 100

# ===========================
# TELA
# ===========================

WIN_WIDTH = 576
WIN_HEIGHT = 324

# ===========================
# POSIÇÃO DO SCORE
# ===========================

SCORE_POS = {

    'Title': (WIN_WIDTH / 2, 40),
    'EnterName': (WIN_WIDTH / 2, 85),
    'Label': (WIN_WIDTH / 2, 110),
    'Name': (WIN_WIDTH / 2, 135),

    0: (WIN_WIDTH / 2, 165),
    1: (WIN_WIDTH / 2, 185),
    2: (WIN_WIDTH / 2, 205),
    3: (WIN_WIDTH / 2, 225),
    4: (WIN_WIDTH / 2, 245),
    5: (WIN_WIDTH / 2, 265),
    6: (WIN_WIDTH / 2, 285),
    7: (WIN_WIDTH / 2, 305),
    8: (WIN_WIDTH / 2, 325),
    9: (WIN_WIDTH / 2, 345),

}
