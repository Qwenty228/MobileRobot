import pygame as pg

pg.init()

SIZE = (640, 640)

window = pg.display.set_mode(SIZE)

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    window.fill('orange')
    pg.display.update()

print("End of program")
pg.quit()