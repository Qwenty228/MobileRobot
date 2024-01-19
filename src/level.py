import pygame as pg
from .enemy import Enemy
import random

class Level:
    def __init__(self, level, player):
        self.level = level
        self.enemies = []
        self.player = player
        self.game_over = False
        for i in range(self.level):
            self.enemies.append(Enemy())
            
    
    def update(self, surface):
        # for enemy in self.enemies:
        #     enemy.update(surface)
        #     for bullet in self.player.bullets:
        #         bullet.update(surface, enemy)
        #         if not(bullet.isalive):
        #             self.player.bullets.remove(bullet) 
        #     if enemy.health == 0: 
        #         self.enemies.remove(enemy)
        for enemy in self.enemies:
            for bullet in self.player.bullets:
                if enemy.rect.collidepoint(bullet.center):
                    enemy.health -= 1
                    bullet.isalive = False
            enemy.update(surface)
            if enemy.health == 0:
                self.enemies.remove(enemy)
            if enemy.rect.y >= 600:
                self.game_over = True
        for bullet in self.player.bullets:
            # for enemy in self.enemies:
            #     bullet.update(surface)
            if not(bullet.isalive):
                self.player.bullets.remove(bullet)
            bullet.update(surface)
        
        
        