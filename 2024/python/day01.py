import numpy as np
from collections import Counter

with open("../inputs/day01.txt") as f:
    ll = f.read().splitlines()

# Part 2
l1 = []
l2 = []

for line in ll:
    line = line.split()
    l1.append(int(line[0]))
    l2.append(int(line[1]))

l1 = np.array(sorted(l1))
l2 = np.array(sorted(l2))

print("Part 1:", sum(abs(l1-l2)))

# Part 2
l1_counts = Counter(l2.tolist())

s = 0
for el in l1.tolist():
    s += el * l1_counts[el]
    
print("Part 2:", s)