import pygame as pg
from src.inertial import Inertial_frame
from src.mrobot import Robot
import numpy as np

FPS = 60

# init 
pg.init()
window = pg.display.set_mode((800, 800), pg.SCALED | pg.RESIZABLE)
pg.display.set_caption("Kinematics")
pg.display.set_icon(pg.image.load("assets/icon.png"))
clock = pg.time.Clock()
iframe = Inertial_frame(window)
robot = Robot((400, 400))
vel = 100 # px/s

movements = np.array([0, 0, 0], dtype=float)


# main loop
running = True
while running:
    # clock
    dt = clock.tick(FPS) * 0.001 
    # events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_d:
                robot.debug = not robot.debug
            if event.key == pg.K_UP:
                movements[0] = 1
            if event.key == pg.K_DOWN:
                movements[0] = -1
            if event.key == pg.K_LEFT:
                movements[1] = -1
            if event.key == pg.K_RIGHT:
                movements[1] = 1
            if event.key == pg.K_q:
                movements[2] = -1
            if event.key == pg.K_e:
                movements[2] = 1
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                movements[0] = 0
            if event.key == pg.K_DOWN:
                movements[0] = 0
            if event.key == pg.K_LEFT:
                movements[1] = 0
            if event.key == pg.K_RIGHT:
                movements[1] = 0
            if event.key == pg.K_q:
                movements[2] = 0
            if event.key == pg.K_e:
                movements[2] = 0


    # draw
    window.fill('gray50')
    iframe.draw()
    robot.update(*vel*movements, dt)
    robot.draw(window)

    
    pg.display.update()
    