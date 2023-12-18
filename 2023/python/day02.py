from collections import defaultdict
from math import prod

data = open("../data/day02.in").read().strip().split("\n")

all_games = set(range(1, len(data) + 1))
impossible_games = []
cubes_needed = []
for (index, game) in enumerate(data):
    d = defaultdict(int)
    records = game.strip().split(":")[1]
    sets = records.split("; ")
    for cube_sets in sets:
        cubes = cube_sets.split(", ")
        for cube in cubes:
            c = cube.strip().split(" ")
            if (c[1] == "red" and int(c[0]) > 12) or (c[1] == "green" and int(c[0]) > 13) or (c[1] == "blue" and int(c[0]) > 14):
                impossible_games.append(index + 1)
            d[c[1]] = int(c[0]) if d[c[1]] < int(c[0]) else d[c[1]]
    cubes_needed.append(d)

impossible_games = set(impossible_games)
print("Sol 1:", sum(all_games - impossible_games))
print("Sol 2:", sum([prod(min_cubes.values()) for min_cubes in cubes_needed]))
