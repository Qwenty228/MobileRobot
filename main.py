import pygame as pg
from src.inertial import Inertial_frame
from src.mrobot import Robot
import numpy as np

<<<<<<< HEAD
FPS = 60

# init 
=======
print("f")
>>>>>>> 1c5f5f457b08c2a3416ad6b8ca42566e952b4648
pg.init()
window = pg.display.set_mode((800, 800), pg.SCALED | pg.RESIZABLE)
pg.display.set_caption("Kinematics")
pg.display.set_icon(pg.image.load("assets/icon.png"))
clock = pg.time.Clock()
iframe = Inertial_frame(window)
robot = Robot((400, 400))
vel = 100 # px/s

<<<<<<< HEAD
movements = np.array([0, 0, 0], dtype=float)
=======
SIZE = WIDTH, HEIGHT = (640, 640)
window = pg.display.set_mode(SIZE)

rect = [320, 320, 100, 100]

run = True

 
>>>>>>> 1c5f5f457b08c2a3416ad6b8ca42566e952b4648


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

<<<<<<< HEAD

    # draw
    window.fill('gray50')
    iframe.draw()
    robot.update(*vel*movements, dt)
    robot.draw(window)

    
=======
    window.fill('grey20')
    pg.draw.rect(window, 'darkgreen', my_button_rect)
    if my_button_rect.collidepoint(pg.mouse.get_pos()):
        pg.draw.rect(window, 'darkred', my_button_rect)
  
>>>>>>> 1c5f5f457b08c2a3416ad6b8ca42566e952b4648
    pg.display.update()
    