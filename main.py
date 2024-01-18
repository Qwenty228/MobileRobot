import pygame as pg

SIZE = (640, 640)

window = pg.display.set_mode(SIZE, pg.RESIZABLE)

pg.display.set_caption("My first game")

rect = [320, 320, 100, 100]

run = True

myRect = pg.Rect([320, 320, 100, 100])
# myRect.center = [320, 320]
banana_surface = pg.image.load("Banana.jpg")
banana_surface = pg.transform.scale(banana_surface, (100, 100))
banana_rect = banana_surface.get_rect()
banana_rect.center = [320, 320]
banana_surface2 = pg.transform.scale(banana_surface, (50, 50))
banana_rect2 = banana_surface2.get_rect()
banana_rect2.center = [50, 50]

while run:
    if myRect.collidepoint(pg.mouse.get_pos()):
        print("Collision")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    window.fill("green")    
    pg.draw.rect(window, "blue", myRect)
    banana_surface.blit(banana_surface2, banana_rect2)
    window.blit(banana_surface, banana_rect)

    # pg.draw.circle(window, "red", (320, 320), 100)
    pg.display.update()

