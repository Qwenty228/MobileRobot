import pygame as pg
import numpy as np 
from math import cos, sin, radians, degrees
from typing import Literal

from src.motor import Motor 

# JACOBIAN = lambda psi: np.array([[cos(psi), -sin(psi), 0], [sin(psi), cos(psi), 0], [0, 0, 1]])
JACOBIAN = lambda psi: np.array([[cos(psi), 0], [sin(psi), 0], [0, 1]])


class Robot:
    def __init__(self, pos) -> None:
        self.pose = np.array((*pos, 0), dtype=float) # contains the x, y, and angle of the robot


        self.image = pg.Surface((100, 50), pg.SRCALPHA)
        self.image.fill('blue')
        pg.draw.polygon(self.image, 'grey28', [(80, 10), (80, 40), (100, 25)])
        arrow = pg.image.load('assets/arrow.png').convert_alpha()
        self.arrow = self.basearrow = pg.transform.scale_by(arrow, 0.5)
        
        self.rect = self.image.get_rect(center=pos)


        self.motors = [Motor(30, 5, 30, 10, self.image), Motor(30, 45, 30, 10, self.image)]

        L = self.rect.width
        self.differential_matrix = np.array([[1, 1], [1/L, -1/L]])/2

        



        self.debug = False
  


        
    def update(self, forward, lateral, rotation, dt=1):
        """forward and lateral are the velocities in the local frame"""
        # forward differential kinematics
        # ἠ = J(ψ)ζ̌     ἠ = [dx, dy, dψ]ᵀ

        # dx, dy, dpsi = dt * (JACOBIAN(self.rad) @ np.array([forward, lateral, rotation], dtype=float))

        # updating the robot state
        if rotation == 1:
            self.motors[0].angular_speed = 5
            self.motors[1].angular_speed = -5
            self.arrow = self.basearrow.copy()
            veloc = np.array([*map(lambda m: m.get_speed(1), self.motors)])
        elif rotation == -1:
            self.motors[0].angular_speed = -5
            self.motors[1].angular_speed = 5
            
            self.arrow = pg.transform.flip(self.basearrow, False, True)
            veloc = np.array([*map(lambda m: m.get_speed(1), self.motors)])
            
        else:
            for motor in self.motors:
                motor.angular_speed = 5
            veloc = np.array([*map(lambda m: m.get_speed(forward), self.motors)])
        speed = JACOBIAN(self.pose[2]) @ self.differential_matrix @ veloc
        self.pose += speed * dt
        self.rect.center = self.pose[:2]
        


    def draw(self, window):
        if self.debug:
            image = pg.transform.rotate(self.arrow, -degrees(self.pose[2]))
            window.blit(image, image.get_rect(center=self.pose[:2]))

        image = pg.transform.rotate(self.image, -degrees(self.pose[2]))
        self.rect = image.get_rect(center=self.pose[:2])
        window.blit(image, self.rect)
      
        # if self.debug: show heading
        #     self.draw_direction(window, 'red', 50*self.fl[0], 'forward')
        #     self.draw_direction(window, 'green', -50*self.fl[1], 'lateral')

    def draw_direction(self, window, color, length=50, direc: Literal['forward', 'lateral']='forward'):
        angle = self.pose[2]
        if direc=="lateral":
            angle -= 90
        x = self.pos[0] + length * cos(angle)
        y = self.pos[1] + length * sin(angle)
        pg.draw.line(window, color, self.pos, (x, y), 2)