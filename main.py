import pygame as pg
from src.tilemap import Tilemap


window = pg.display.set_mode((800, 600))
tm = Tilemap("data/map.json")



clock = pg.time.Clock()

run = True

player_pos = [0, 0]

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    player_pos[0] += 1
    
    
    window.fill((0, 0, 0))

    tm.draw_map(window, player_pos)

    pg.display.update()
    clock.tick(60)