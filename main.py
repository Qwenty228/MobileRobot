import pygame as pg
import random

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
    def __init__(self, color, radius, pos, level):
        self.center = pos
        self.radius = radius
        self.color = color
        self.bullets = []
        self.enemies = []
        for i in range(level):
            self.enemies.append(Enemy())
    
    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.center, self.radius)

    def update(self,surface):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.center[0] -= 5
        if keys[pg.K_RIGHT]:
            self.center[0] += 5
        for enemy in self.enemies:
            enemy.update(surface)
            for bullet in self.bullets:
                bullet.update(surface, enemy)
                if not(bullet.isalive):
                    self.bullets.remove(bullet) 
            if enemy.health == 0: 
                self.enemies.remove(enemy)
                
                
    
    def fire(self):
        self.bullets.append(Bullet([self.center[0], self.center[1]]))

class Bullet:
    def __init__(self, pos):
        self.center = pos
        self.color = "white"
        self.radius = 4
        self.isalive = True

    def update(self, surface, enemy):
        self.center[1] -= 2
        pg.draw.circle(surface, self.color, (self.center[0], self.center[1]), self.radius)
        if not((0 <= self.center[0] <= WIDTH) and (0 <= self.center[1] <= HEIGHT)):
            self.isalive = False
        if enemy.rect.collidepoint(self.center):
            enemy.health -= 1
            self.isalive = False

class Enemy:
    def __init__(self):
        self.color = "grey"
        self.surface = pg.Surface((30, 30))
        self.rect = self.surface.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, 200))
        self.health = 3

    
    def update(self, surface):
        if self.health == 2:
            self.color = "orange"
        elif self.health == 1:
            self.color = "red"
        surface.blit(self.surface, self.rect)
        self.surface.fill(self.color)
        

clock = pg.time.Clock()


my_player = Player('red', 10, [100, 600],2)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                my_player.fire()


    window.fill('black')


    my_player.draw(window)
    my_player.update(window)
    pg.display.update()
    clock.tick(60)

print("End of program")
pg.quit()