import numpy as np
import pygame as pg

from .settings import *

class Camera:
    def __init__(self) -> None:
        self.scroll = np.array((0, 0), dtype=np.float32)

    def update(self, target_pos: pg.Vector2, screen_size: tuple[int, int]) -> tuple[int, int]:
         # camera formula: scroll increment by:  (target position - last scroll position)/ camera speed
        self.scroll[0] += (target_pos.centerx - screen_size[0]/2 - self.scroll[0]) / 25
        self.scroll[1] += (target_pos.centery - screen_size[1]/2 - self.scroll[1]) / 25

        # returning the top left position of the camera as a map coordinate
        return int(self.scroll[0]), int(self.scroll[1])




class Mouse:
    offset = (0, 0)
    pos = (0, 0)
    ratio = 1
    @classmethod
    def update(cls):
        x, y = pg.mouse.get_pos()
        cls.pos = (x - cls.offset[0]) /cls.ratio , (y - cls.offset[1] )/ cls.ratio