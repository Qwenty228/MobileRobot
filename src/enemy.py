import pygame as pg
import random

SIZE = WIDTH, HEIGHT = (640, 640)

class Enemy:
    def __init__(self):
        self.color = "grey"
        self.surface = pg.Surface((30, 30))
        self.rect = self.surface.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, 200))
        self.health = 3

    
    def update(self, surface):
        self.rect.y += 0.5
        if self.health == 2:
            self.color = "orange"
        elif self.health == 1:
            self.color = "red"
        surface.blit(self.surface, self.rect)
        self.surface.fill(self.color)