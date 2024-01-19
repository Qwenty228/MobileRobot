import pygame as pg

from src.camera import Camera
from src.tilemap import Tilemap
from src.settings import *
from src.player import Player
from shader.core import Shader

window = pg.display.set_mode(SIZE, pg.OPENGL|pg.DOUBLEBUF|pg.RESIZABLE)
display = pg.Surface(SIZE)

tm = Tilemap("data/map.json")


camera = Camera()
shader = Shader()
clock = pg.time.Clock()
run = True



player = Player((0, 0, TILESIZE, TILESIZE), 'red')
movement = [False, False, False, False]

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.VIDEORESIZE:
            shader.screen_size = event.size
            shader.min_ratio = min(HEIGHT/event.h, WIDTH/event.w)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_F11:
                pg.display.toggle_fullscreen()
            if event.key == pg.K_a:
                movement[0] = True
            if event.key == pg.K_d:
                movement[1] = True
            if event.key == pg.K_w:
                movement[2] = True
            if event.key == pg.K_s:
                movement[3] = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                movement[0] = False
            if event.key == pg.K_d:
                movement[1] = False
            if event.key == pg.K_w:
                movement[2] = False
            if event.key == pg.K_s:
                movement[3] = False

    dt = clock.tick(60) * 0.001   
    pg.display.set_caption(f"FPS: {clock.get_fps():.2f}") 

    render_scroll = camera.update(player.rect, SIZE)
    display.fill('black')
    tm.render(display, render_scroll)
    player.update(tm, (movement[1] - movement[0], movement[3] - movement[2]), dt=dt)
    player.draw(display, offset=render_scroll)

    shader.render(display)
    pg.display.flip()
    