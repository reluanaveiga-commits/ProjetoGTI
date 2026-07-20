from code.EnemyShot import EnemyShot
from code.Const import WIN_WIDTH
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
from code.Obstacle import Obstacle


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):

        # inimigo saiu da tela
        if isinstance(ent, Enemy):

            if ent.rect.right < 0:

                ent.health = 0


        # obstáculo saiu da tela
        if isinstance(ent, Obstacle):

            if ent.rect.right < 0:

                ent.health = 0



        # tiro jogador saiu da tela
        if isinstance(ent, PlayerShot):

            if ent.rect.left > WIN_WIDTH or ent.rect.right < 0:

                ent.health = 0



        # tiro inimigo saiu da tela
        if isinstance(ent, EnemyShot):

            if ent.rect.left < 0 or ent.rect.right > WIN_WIDTH:

                ent.health = 0




    @staticmethod
    def __verify_collision_entity(ent1, ent2):

        if ent1.rect.colliderect(ent2.rect):


            # =========================
            # PLAYER X ENEMY
            # =========================

            if isinstance(ent1, Player) and isinstance(ent2, Enemy):

                ent1.health -= ent2.damage

                ent2.health = 0

                ent1.last_dmg = ent2.name



            elif isinstance(ent1, Enemy) and isinstance(ent2, Player):

                ent2.health -= ent1.damage

                ent1.health = 0

                ent2.last_dmg = ent1.name




            # =========================
            # PLAYER X OBSTACLE
            # =========================

            elif isinstance(ent1, Player) and isinstance(ent2, Obstacle):

                ent1.health -= ent2.damage

                ent2.health = 0

                ent1.last_dmg = ent2.name



            elif isinstance(ent1, Obstacle) and isinstance(ent2, Player):

                ent2.health -= ent1.damage

                ent1.health = 0

                ent2.last_dmg = ent1.name





            # =========================
            # TIRO PLAYER X ENEMY
            # =========================

            elif isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):

                ent1.health -= ent2.damage

                ent2.health = 0

                ent1.last_dmg = ent2.name



            elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):

                ent2.health -= ent1.damage

                ent1.health = 0

                ent2.last_dmg = ent1.name




            # =========================
            # TIRO INIMIGO X PLAYER
            # =========================

            elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):

                ent1.health -= ent2.damage

                ent2.health = 0

                ent1.last_dmg = ent2.name



            elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):

                ent2.health -= ent1.damage

                ent1.health = 0

                ent2.last_dmg = ent1.name





    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):

        if enemy.last_dmg == 'Player1Shot':

            for ent in entity_list:

                if ent.name == 'Player1':

                    ent.score += enemy.score





    @staticmethod
    def verify_collision(entity_list: list[Entity]):

        for i in range(len(entity_list)):

            entity1 = entity_list[i]


            EntityMediator.__verify_collision_window(entity1)



            for j in range(i + 1, len(entity_list)):

                entity2 = entity_list[j]


                EntityMediator.__verify_collision_entity(
                    entity1,
                    entity2
                )






    @staticmethod
    def verify_health(entity_list: list[Entity]):

        for ent in entity_list[:]:


            if ent.health <= 0:


                if isinstance(ent, Enemy):

                    EntityMediator.__give_score(
                        ent,
                        entity_list
                    )


                entity_list.remove(ent)