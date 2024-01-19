import random
from pygame.sprite import Group
import pygame as pg
from pygame import Vector2

from .entities import Entity
from .settings import TILESIZE
from .tools import Mouse


class Timer:
    def __init__(self, interval, callback=lambda: None):
        self.interval = interval
        self.callback = callback
        self.time = interval
        self.activated = False

    def activate(self):
        self.activated = True


    def update(self, dt):
        if self.activated:
            self.time -= dt
            self.callback()
            if self.time <= 0:
                self.time = self.interval
                self.activated = False
        


def swing_sword():
    """generator"""
    while True:
        for i in range(random.randint(-30, 0), random.randint(60, 100), 1):
            yield i
swing = swing_sword()


class Sword:
    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((48, 20), pg.SRCALPHA)
        self.image.fill('purple')

        # A reference to the original image to preserve the quality.
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)  # The original center position/pivot point.
        self.offset = Vector2(40, 0)  # We shift the sprite 50 px to the right.
        self.angle = 0
        self.timers = {"swing": Timer(0.1, self.reset_angle), "cooldown": Timer(0.3)}

    def update(self, player_pos):
        """Update the pivot position and the rect."""
        self.pos = Vector2(player_pos)
        self.rect = self.image.get_rect(center=self.pos)

    def rotate(self):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pg.transform.rotozoom(self.orig_image, -self.angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos+offset_rotated)

    def reset_angle(self):
        self.angle += next(swing)

    def draw(self, surf, offset=(0, 0)):
        surf.blit(self.image, (self.rect.x - offset[0], self.rect.y - offset[1]))



class Gun:
    def __init__(self) -> None:
        self.rect = pg.Rect(0, 0, 10, 10)
        self.image = pg.Surface((10, 10))
        self.image.fill('red')

    def update(self, pos, line):
        self.rect.center = pos
        self.rect.x += line.x /10
        self.rect.y += line.y /10

    def draw(self, surf, offset=(0, 0)):
        surf.blit(self.image, (self.rect.x - offset[0], self.rect.y - offset[1]))


class Player(Entity):
    def __init__(self, rect, image, group: Group = None, zombies=[]) -> None:
        super().__init__(rect, image, group)
        self.speed = 160
        self.zombies = zombies
        self.sword = Sword(self.rect.center)
        # self.gun = Gun()
        self.timers = {"dash cooldown": Timer(1)}
       

    def update(self, tilemap, movement=(0, 0), dt=1):
        super().update(tilemap, movement, dt)
        
        self.sword.update(self.rect.center)
        if pg.mouse.get_pressed()[0] and not self.sword.timers["cooldown"].activated:
            self.sword.timers["swing"].activate()
            self.sword.timers["cooldown"].activate()
            for zombie in self.zombies:
                if self.sword.rect.colliderect(zombie.rect):
                    zombie.hp -= 10
                    if zombie.hp <= 0:
                        self.zombies.remove(zombie)
        
        if not self.timers["dash cooldown"].activated:
            keys = pg.key.get_pressed()
            if keys[pg.K_LSHIFT]:
                self.pos.x += 200
                self.timers["dash cooldown"].activate()
       
        self.timers["dash cooldown"].update(dt)
        self.sword.timers["swing"].update(dt)
        self.sword.timers["cooldown"].update(dt)
        

   
    def draw(self, surf, offset=(0, 0)):
        super().draw(surf, offset)
        pivot = Vector2(self.rect.center) - Vector2(offset)
        line = pivot - Vector2(Mouse.pos)

        


        if not self.sword.timers["swing"].activated:
            self.sword.angle = 180-line.angle_to(Vector2(1, 0))
        self.sword.rotate()
        if self.sword:
            self.sword.draw(surf, offset)
