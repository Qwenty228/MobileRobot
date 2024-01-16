import pygame as pg

print("f")
pg.init()

SIZE = WIDTH, HEIGHT = (640, 640)
window = pg.display.set_mode(SIZE)

rect = [320, 320, 100, 100]

run = True

 




# rect1 = MyRect([100, 100, 100, 100], 'darkgreen')

my_button_rect = pg.Rect([100,100,100,100])
my_button_rect.center = WIDTH/2, HEIGHT/2



while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    window.fill('grey20')
    pg.draw.rect(window, 'darkgreen', my_button_rect)
    if my_button_rect.collidepoint(pg.mouse.get_pos()):
        pg.draw.rect(window, 'darkred', my_button_rect)
  
    pg.display.update()


print("End of program")
pg.quit()