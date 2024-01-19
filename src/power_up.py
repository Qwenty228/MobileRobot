import pygame as pg
import random

SIZE = WIDTH, HEIGHT = (640, 640)

class Power_up:
    def __init__(self, type):
        self.type = random.randint(1, 2)
        self.surface = pg.Surface((20, 20))
        self.rect = self.surface.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), 600)
    
    def update(self, surface):
        if self.type == 1:
            