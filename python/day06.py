import re
from math import prod

data = open("../data/day06.in").read().strip().split("\n")

seconds = list(map(int, re.findall(r"\d+", data[0])))
distances = list(map(int,re.findall(r"\d+", data[1])))

possible = [0 for _ in range(len(seconds))]
for i in range(len(seconds)):
    for hold in range(1, seconds[i]):
        if  (hold * (seconds[i] - hold)) > distances[i]:
            possible[i] += 1
print("Sol 1:", prod(possible))

seconds = re.findall(r"\d+", data[0])
distances = re.findall(r"\d+", data[1])
s = int("".join(seconds))
d = int("".join(distances))
p = 0
for hold in range(1, s):
    if  (hold * (s - hold)) > d:
        p += 1
print("Sol 2:", p)