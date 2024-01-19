

# map structure:
# { tiles: {"x;y":[name, orientation, layer]}, decorations: {"x;y":[name, orientation, layer]}}


import random
import json


data = {"tiles": {}, "decorations": {}}

tiles = ["grass", 'stone', 'sand']

for x in range(-100, 100):
    for y in range(-100, 100):
        data["tiles"][str(x) + ";" + str(y)] = [random.choice(tiles), 0, 0]


with open("data/map.json", "w") as f:
    json.dump(data, f, indent=2)
    
