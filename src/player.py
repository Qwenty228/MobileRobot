import pygame as pg 
from .bullet import Bullet
from .power_up import Power_up



class Player:
    def __init__(self, color, radius, pos, level):
        self.center = pos
        self.radius = radius
        self.color = color
        self.bullets = []
        self.powerups = []
        

    def update(self,surface):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.center[0] -= 5
        if keys[pg.K_RIGHT]:
            self.center[0] += 5
        pg.draw.circle(surface, self.color, self.center, self.radius)        
                
                
    
    def fire(self):
        self.bullets.append(Bullet([self.center[0], self.center[1]]))