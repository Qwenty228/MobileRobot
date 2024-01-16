import pygame as pg

pg.init()

SIZE = (640, 640)

window = pg.display.set_mode(SIZE)

run = True

rect = [100, 100, 100, 100]

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    window.fill('orange')
    
    pg.draw.rect(window, 'red', (100, 100, 100, 100))

    

    
    pg.display.update()


print("End of program")
pg.quit()