import pygame as pg
from src.fonts import Font


class Control:
    def __init__(self, window) -> None:
        self.window =window
        self.surface = pg.Surface((self.window.get_width(), self.window.get_height()*0.2), pg.SRCALPHA)
        self.rect = self.surface.get_rect(topright=(self.window.get_width(), 0))
        
        self.font = Font('consolas', 40)
        
        self.font.render_to(self.surface, (10, 60), 'd: toggle debug', 'darkgreen')
        self.font.render_to(self.surface, (10, 100), 'up, down: forward, backward', 'darkgreen')
        self.font.render_to(self.surface, (10, 140), 'left, right: left, right', 'darkgreen')
        self.font.render_to(self.surface, (10, 180), 'q, e: rotate', 'darkgreen')

    def draw(self):
        self.window.blit(self.surface, self.rect)

class Inertial_frame:
    def __init__(self, window):
        self.window = window
        self.win_size = window.get_size()
        self.surface = pg.Surface((self.win_size[0]*0.2, self.win_size[1]*0.2))
        self.size = self.w, self.h = self.surface.get_size()
        self.rect = self.surface.get_rect(bottomleft=(0, self.win_size[1]))
        self.surface.fill('white')

        self.direction_line((self.w/2 - 5, self.h/2 + 5), 0, 'red')
        self.direction_line((self.w/2 - 5, self.h/2 + 5), -90, 'green')
        Font('consolas', 20).render_to(self.surface, (self.w*0.75, self.h/2 - 10), 'x', 'red')
        Font('consolas', 20).render_to(self.surface, (self.w/2 - 20, self.h*0.25), 'y', 'green')

        self.control = Control(self.window)

    
    def direction_line(self, pos, angle, color):
        x = pos[0] + self.w/2 * pg.math.Vector2(1, 0).rotate(angle)[0]
        y = pos[1] + self.h/2 * pg.math.Vector2(1, 0).rotate(angle)[1]
        pg.draw.line(self.surface, color, pos, (x, y), 2)
        pg.draw.circle(self.surface, color, (int(x), int(y)), 5)


    def draw(self):
        self.window.blit(self.surface, self.rect)
        self.control.draw()
     