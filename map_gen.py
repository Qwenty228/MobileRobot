

# map structure:
# { data: {"x;y":[name, orientation, layer]}}


import random
import json

data = {"data": {}}

tiles = ["grass", 'stone', 'sand']

for x in range(-10, 10):
    for y in range(-10, 10):
        data["data"][str(x) + ";" + str(y)] = [random.choice(tiles), 0, 0]


with open("data/map.json", "w") as f:
    json.dump(data, f, indent=2)
    
