import pygame as pg
from pygame import Vector2



class Entity(pg.sprite.Sprite):
    def __init__(self, rect, image, group: pg.sprite.Group = None) -> None:
        if group:
            group.add(self)
        super().__init__()
        self.image = pg.Surface(rect[2:])
        self.image.fill(image)
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


