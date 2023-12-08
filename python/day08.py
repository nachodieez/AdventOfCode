import re
from math import lcm

data = open("../data/day08.in").read().strip().split("\n\n")

data[0] = data[0].replace("L", "0").replace("R", "1")

d = {}
for line in data[1].split("\n"):
    a, b, c = re.findall(r"\w+", line)
    d[a] = (b, c)

current = "AAA"
steps = 0
while current != "ZZZ":
    for i in data[0]:
        current = d[current][int(i)]
        steps += 1
        if current == "ZZZ":
            break
print("Sol 1:", steps)

current = [node for node in d if node.endswith("A")]
steps = [0 for _ in range(len(current))]

for node in range(len(current)):
    while not(current[node].endswith("Z")):
        for i in data[0]:
            current[node] = d[current[node]][int(i)]
            steps[node] += 1
            if current[node].endswith("Z"):
                break
print("Sol 2:", lcm(*steps))