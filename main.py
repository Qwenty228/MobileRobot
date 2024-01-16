import pygame as pg

print("f")
pg.init()

SIZE = WIDTH, HEIGHT = (640, 640)

window = pg.display.set_mode(SIZE)

my_rect = pg.Rect([100, 100, 100, 100])
my_rect.center = WIDTH/2, HEIGHT/2

run = True

# surface = pg.Surface(my_rect.size)
surface = pg.image.load('pic.png')

clock = pg.time.Clock()


while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        my_rect.x -= 10
    if keys[pg.K_RIGHT]:
        my_rect.x += 10
    if keys[pg.K_UP]:
        my_rect.y -= 10
    if keys[pg.K_DOWN]:
        my_rect.y += 10

    window.fill('orange')
    window.blit(surface, my_rect)
    # if my_rect.collidepoint(pg.mouse.get_pos()):
    #     surface.fill("red")
    # else:


    # window.blit(surface, my_rect)
    # pg.draw.rect(window, 'blue', my_rect)
    # if my_rect.collidepoint(pg.mouse.get_pos()):
    #     pg.draw.rect(window, 'red', my_rect)

    # if (rect[0] <= pg.mouse.get_pos()[0] <= rect[0] + rect[2]) and (rect[1] <= pg.mouse.get_pos()[1] <= rect[1] + rect[3]):
    #     print("Collide")
    # print(pg.mouse.get_pos())
    pg.display.update()
    clock.tick(60)

print("End of program")
pg.quit()