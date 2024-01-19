import pygame as pg
import json


from .settings import *





TILESIZE = 32

TILES_W = WIDTH // TILESIZE
TILES_H = HEIGHT // TILESIZE




class Tilemap:
    def __init__(self, path: str) -> None:
        try: 
            with open(path, "r") as f:
                self.map = json.load(f)
        except FileNotFoundError:
            print("Map file not found!")
            self.map = {"data": {"0;0": ["grass", 0, 0]}}


        self.TILES = {"grass": (self.create_tile('green'), 0, 0),
                      "stone": (self.create_tile('gray'), 0, 0),
                      "sand": (self.create_tile('yellow'), 0, 0)}

    def create_tile(self, color):
        tile = pg.Surface((TILESIZE, TILESIZE))
        tile.fill(color)
        pg.draw.rect(tile, 'black', (0, 0, TILESIZE, TILESIZE), 1)
        return tile


    def draw_map(self, surface, player_pos: tuple[int, int]) -> None:
        for x in range(TILES_W + 1):
            for y in range(TILES_H + 1):    
                tile = self.map["data"].get(str(x + player_pos[0]//TILESIZE) + ";" + str(y + player_pos[1]//TILESIZE))
                if tile:
                    surface.blit(self.TILES[tile[0]][0], (x * TILESIZE+ player_pos[0] % TILESIZE, y * TILESIZE + player_pos[1]%TILESIZE))
                  