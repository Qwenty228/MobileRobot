import pygame as pg
from pygame import Vector2
from pygame.sprite import Group



class Entity(pg.sprite.Sprite):
    def __init__(self, rect, image, group: pg.sprite.Group = None) -> None:
        if group:
            group.add(self)
        super().__init__()
        self.image = pg.Surface(rect[2:])
        try:
            self.image.fill(image)
        except TypeError:
            pass
        self.rect = self.image.get_rect(topleft=rect[:2])

        self._pos = Vector2(self.rect.topleft) # more precise position
        self.speed = 160 # pixels per second

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = Vector2(value)
        self.rect.topleft = self.pos


    def update(self, tilemap, movement=(0, 0), dt=1):
        if movement != (0, 0):
            self.pos += Vector2(movement).normalize() * self.speed * dt
   
      
    def draw(self, surf, offset=(0, 0)):
        surf.blit(self.image, (self.pos.x - offset[0], self.pos.y - offset[1]))



class Zombie(Entity):
    img = None
    def __init__(self, rect, image, group: Group = None) -> None:
        super().__init__(rect, (0, 0,0 ,0), group)
        if not Zombie.img:
            Zombie.img = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(Zombie.img, rect[2:])

        self.movement = Vector2(0, 0)
        self.speed = 80
        self.hp = 100

    def draw_health(self, surf, offset=(0, 0)):
        width = self.rect.width * self.hp / 100
        pg.draw.rect(surf, 'red', (self.rect.x - offset[0], self.rect.y - offset[1] - 10, width, 5))

    def update(self, tilemap, dt=1):
        super().update(tilemap, self.movement, dt)

    def draw(self, surf, offset=(0, 0)):
        super().draw(surf, offset)
        self.draw_health(surf, offset)