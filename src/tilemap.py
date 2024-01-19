import pygame as pg
import json


from .settings import *





class Tilemap:
    def __init__(self, path: str) -> None:
        try: 
            with open(path, "r") as f:
                self.map = json.load(f)
        except FileNotFoundError:
            print("Map file not found!")
            self.map = {"data": {"0;0": ["grass", 0, 0]}}


        self.TILES = {"grass": self.create_tile('green'),
                      "stone": self.create_tile('gray'),
                      "sand": self.create_tile('yellow')}

    def create_tile(self, color):
        tile = pg.Surface((TILESIZE, TILESIZE))
        tile.fill(color)
        pg.draw.rect(tile, 'black', (0, 0, TILESIZE, TILESIZE), 1)
        return tile


    def render(self, surf, offset=(0, 0)):
        # for tile in self.offgrid_tiles:
        #     # usually are decorations, like trees, rocks, etc.
        #     surf.blit(self.game.assets[tile['type']][tile['variant']][0],
        #               (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))
        for x in range(offset[0]//TILESIZE, (offset[0] + WIDTH)//TILESIZE + 1):
            for y in range(offset[1]//TILESIZE, (offset[1] + HEIGHT)//TILESIZE + 1):
                if (tileinfo := self.map["tiles"].get(f'{x};{y}')) is not None:
                    tile_name, orientation, layer = tileinfo
                    surf.blit(self.TILES[tile_name], (x * TILESIZE - offset[0], y * TILESIZE - offset[1]))