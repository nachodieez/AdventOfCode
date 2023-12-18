import numpy as np
import re

data = open("../data/day09.in").read().strip().split("\n")

res = []
for line in data:
    lines = []
    lines.append(np.array([int(number) for number in line.split(" ")], dtype=np.int32))
    while not(np.all(lines[-1] == 0)) and (len(np.diff(lines[-1])) > 0):
        lines.append(np.diff(lines[-1]))
    lines[-1] = np.append(lines[-1], 0)
    lines = list(reversed(lines))
    for i in range(1, len(lines)):
        lines[i] = np.append(lines[i], lines[i-1][-1] + lines[i][-1])
    res.append(lines[-1][-1])
print("Sol 1:", np.sum(res))   

res = []
for line in data:
    lines = []
    lines.append(np.array([int(number) for number in line.split(" ")], dtype=np.int32))
    while not(np.all(lines[-1] == 0)) and (len(np.diff(lines[-1])) > 0):
        lines.append(np.diff(lines[-1]))
    lines[-1] = np.append(0, lines[-1])
    lines = list(reversed(lines))
    for i in range(1, len(lines)):
        lines[i] = np.append(lines[i][0] - lines[i-1][0], lines[i])
    res.append(lines[-1][0])
print("Sol 2:", np.sum(res))   