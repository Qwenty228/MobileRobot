import pygame.freetype 
import pygame as pg

pg.freetype.init()

class Font:
    fonts = {}
    def __new__(cls, name, size):
        if name not in cls.fonts:
            try:
                cls.fonts[name] = pg.freetype.Font(name, size)
            except FileNotFoundError:
                cls.fonts[name] = pg.freetype.SysFont(name, size)
        return cls.fonts[name]