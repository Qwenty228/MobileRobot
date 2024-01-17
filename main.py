import pygame as pg

print("f")
pg.init()

SIZE = WIDTH, HEIGHT = (640, 640)

window = pg.display.set_mode(SIZE)
pg.display.set_caption("Space Invaders")

my_rect = pg.Rect([100, 100, 100, 100])
my_rect.center = WIDTH/2, HEIGHT/2

run = True

font = pg.font.SysFont('Arial', 38)

class Player:
    def __init__(self, color, radius, pos):
        self.center = pos
        self.radius = radius
        self.color = color
        self.bullets = []
    
    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.center, self.radius)

    def update(self,surface):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.center[0] -= 5
        if keys[pg.K_RIGHT]:
            self.center[0] += 5
        # if keys[pg.K_UP]:
        #     self.center[1] -= 5
        # if keys[pg.K_DOWN]:
        #     self.center[1] += 5
        # if keys[pg.K_SPACE]:
        #     self.bullets.append(Bullet([self.center[0], self.center[1]]))
        for bullet in self.bullets:
            bullet.update(surface)
    
    def fire(self):
        self.bullets.append(Bullet([self.center[0], self.center[1]]))

class Bullet:
    def __init__(self, pos):
        self.center = pos
        self.color = "white"
        self.radius = 4

    def update(self, surface):
        self.center[1] -= 2
        pg.draw.circle(surface, self.color, (self.center[0], self.center[1]), self.radius)

clock = pg.time.Clock()


my_player = Player('red', 10, [100, 600])

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                my_player.fire()
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         my_button.click_event(pg.mouse.get_pos(), True)
        #         button.click_event(pg.mouse.get_pos(), True)


    window.fill('black')


    my_player.draw(window)
    my_player.update(window)

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