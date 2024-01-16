import pygame as pg
import numpy as np 
from math import cos, sin, radians
from typing import Literal

JACOBIAN = lambda psi: np.array([[cos(psi), -sin(psi), 0], [sin(psi), cos(psi), 0], [0, 0, 1]])

class Robot:
    def __init__(self, pos) -> None:
        self.pos = np.array(pos, dtype=float)
        self.angle = 0  # degrees
        self.size = self.w, self.h = 60, 30
        self.image = pg.Surface(self.size, pg.SRCALPHA)
        self.rect = self.image.get_rect(center=self.pos) # ref point is at center

        self.image.fill('blue')
        car_front = pg.Surface((self.w*0.1, self.h))
        car_front.fill('black')
        self.image.blit(car_front, (self.w*0.8, 0))
        

        self.debug = False

  
    @property
    def rad(self):
        return radians(self.angle)
    

        
    def update(self, forward, lateral, rotation, dt=1):
        """forward and lateral are the velocities in the local frame"""
        # forward differential kinematics
        # ἠ = J(ψ)ζ̌     ἠ = [dx, dy, dψ]ᵀ
        dx, dy, dpsi = dt * (JACOBIAN(self.rad) @ np.array([forward, lateral, rotation], dtype=float))

        # updating the robot state
        self.pos += dx, dy
        self.angle += dpsi


    def draw(self, window):
        image = pg.transform.rotate(self.image, -self.angle)
        self.rect = image.get_rect(center=self.pos)
        window.blit(image, self.rect)
        if self.debug:
            self.draw_direction(window, 'red', 50, 'forward')
            self.draw_direction(window, 'green', -50, 'lateral')

    def draw_direction(self, window, color, length=50, direc: Literal['forward', 'lateral']='forward'):
        angle = self.angle
        if direc=="lateral":
            angle -= 90
        x = self.pos[0] + length * cos(radians(angle))
        y = self.pos[1] + length * sin(radians(angle))
        pg.draw.line(window, color, self.pos, (x, y), 2)