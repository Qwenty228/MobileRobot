import pygame as pg

pg.init()

SIZE = (640, 640)

window = pg.display.set_mode(SIZE)

rect = [320, 320, 100, 100]

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    window.fill('orange')
    pg.draw.rect(window, 'blue', rect, border_top_left_radius=20, border_bottom_right_radius=20, width=2)
    if (rect[0] <= pg.mouse.get_pos()[0] <= rect[0] + rect[2]) and (rect[1] <= pg.mouse.get_pos()[1] <= rect[1] + rect[3]):
        print("Collide")
    # print(pg.mouse.get_pos())
    pg.display.update()

print("End of program")
pg.quit()