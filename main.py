import pygame as pg
import random
from src.bullet import Bullet
from src.level import Level
from src.player import Player
from src.enemy import Enemy

print("f")
pg.init()

SIZE = WIDTH, HEIGHT = (640, 640)

window = pg.display.set_mode(SIZE)
pg.display.set_caption("Space Invaders")

my_rect = pg.Rect([100, 100, 100, 100])
my_rect.center = WIDTH/2, HEIGHT/2

run = True

font = pg.font.SysFont('Arial', 38)      

clock = pg.time.Clock()


my_player = Player('red', 10, [100, 600],2)
my_level = Level(100, my_player)

while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    my_player.fire()


        window.fill('black')

        my_level.update(window)  
        my_player.update(window)
        if my_level.game_over:
             run = False
        pg.display.update()
        clock.tick(60)

print("End of program")
pg.quit()