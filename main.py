import pygame as pg

from src.camera import Camera
from src.tilemap import Tilemap
from src.settings import *
from shader.core import Shader

window = pg.display.set_mode(SIZE, pg.OPENGL|pg.DOUBLEBUF|pg.RESIZABLE)
display = pg.Surface(SIZE)

tm = Tilemap("data/map.json")


camera = Camera()
shader = Shader()
clock = pg.time.Clock()
run = True

player_pos = pg.Rect(0, 0, 32, 32)


while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.VIDEORESIZE:
            shader.screen_size = event.size
            shader.min_ratio = min(HEIGHT/event.h, WIDTH/event.w)

    dt = clock.tick(60) * 0.001    



    render_scroll = camera.update(player_pos, SIZE)
    display.fill('white')
    tm.render(display, render_scroll)
    pg.draw.circle(display, 'red', (player_pos.x - render_scroll[0], player_pos.y - render_scroll[1]), 16)
    
    shader.render(display)
    pg.display.flip()
    