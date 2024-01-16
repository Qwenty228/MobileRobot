import pygame as pg

print("f")
pg.init()

SIZE = WIDTH, HEIGHT = (640, 640)

window = pg.display.set_mode(SIZE)

my_rect = pg.Rect([100, 100, 100, 100])
my_rect.center = WIDTH/2, HEIGHT/2

run = True

font = pg.font.SysFont('Arial', 38)

class Button:
    def __init__(self, color, rect) -> None:
        self.surface = pg.Surface((rect[2], rect[3]))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.center = rect[0], rect[1]
        self.color = color
        self.activated = False
        self.text_surface = font.render("Clickkkkkkkkkkkkkkkkkkkkkkkkkkk", True, "White")
        self.text_rect = self.text_surface.get_rect(center = self.rect.center)
    
    def draw(self, surface):
        if self.activated:
            self.surface.fill("black")
        else:
            self.surface.fill(self.color)
        self.activated = False
        surface.blit(self.surface, self.rect)
        surface.blit(self.text_surface, self.text_rect)
        

    def click_event(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed:
                self.activated = True
                self.activate()
            
    
    def activate(self):
        print("yo")
        # self.surface.fill(self.color)

# surface = pg.Surface(my_rect.size)

my_button = Button("red", [100, 100, 100, 100])
button = Button("blue", [200, 200, 100, 100])
clock = pg.time.Clock()


while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                my_button.click_event(pg.mouse.get_pos(), True)
                button.click_event(pg.mouse.get_pos(), True)

    
    # keys = pg.key.get_pressed()
    # if keys[pg.K_LEFT]:
    #     my_rect.x -= 10
    # if keys[pg.K_RIGHT]:
    #     my_rect.x += 10
    # if keys[pg.K_UP]:
    #     my_rect.y -= 10
    # if keys[pg.K_DOWN]:
    #     my_rect.y += 10

    window.fill('orange')

    my_button.draw(window)
    button.draw(window)
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