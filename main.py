import pygame as pg

print("f")
pg.init()

SIZE = WIDTH, HEIGHT = (640, 640)

window = pg.display.set_mode(SIZE)

my_rect = pg.Rect([100, 100, 100, 100])
my_rect.center = WIDTH/2, HEIGHT/2

run = True

font = pg.font.SysFont('Arial', 38)

class Player:
    def __init__(self, color, radius, pos):
        self.center = pos
        self.radius = radius
        self.color = color
    
    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.center, self.radius)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.center[0] -= 10
        if keys[pg.K_RIGHT]:
            self.center[0] += 10
        if keys[pg.K_UP]:
            self.center[1] -= 10
        if keys[pg.K_DOWN]:
            self.center[1] += 10

clock = pg.time.Clock()


my_player = Player('red', 10, [100, 100])

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         my_button.click_event(pg.mouse.get_pos(), True)
        #         button.click_event(pg.mouse.get_pos(), True)


    window.fill('black')

    my_player.draw(window)
    my_player.update()

    # my_button.draw(window)
    # button.draw(window)
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