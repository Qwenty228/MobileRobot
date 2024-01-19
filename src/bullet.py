import pygame as pg 

SIZE = WIDTH, HEIGHT = (640, 640)

class Bullet:
    def __init__(self, pos):
        self.center = pos
        self.color = "white"
        self.radius = 4
        self.isalive = True

    def update(self, surface):
        self.center[1] -= 2
        pg.draw.circle(surface, self.color, (self.center[0], self.center[1]), self.radius)
        if not((0 <= self.center[0] <= WIDTH) and (0 <= self.center[1] <= HEIGHT)):
            self.isalive = False
        