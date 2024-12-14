import numpy as np
import sys
from matplotlib import pyplot as plt

with open("../inputs/day14.txt") as f:
    ll = [x.strip() for x in f.readlines()]

wide = 101
tall = 103
seconds = 100

final_positions = []
for line in ll:
    pos, vel = line.split(" v=")
    pos = pos.split("p=")[1]
    
    pos = tuple(map(int, pos.split(",")))
    vel = tuple(map(int, vel.split(",")))
    
    pos_x = (pos[0] + vel[0] * seconds)
    pos_y = (pos[1] + vel[1] * seconds)
    
    positions = [pos_x, pos_y]
    for i in range(len(positions)):
        to_divide = wide if i == 0 else tall
        if positions[i] < 0:
            positions[i] = (positions[i] % to_divide)
        else:
            positions[i] = (positions[i] % to_divide)

    final_positions.append(positions)
    
quadrants_count = [0] * 4

middle_wide = wide // 2
middle_tall = tall // 2

for robot in final_positions:
    if robot[0] < middle_wide and robot[1] < middle_tall:
        quadrants_count[0] += 1
    elif robot[0] < middle_wide and robot[1] > middle_tall:
        quadrants_count[2] += 1
    elif robot[0] > middle_wide and robot[1] < middle_tall:
        quadrants_count[1] += 1
    elif robot[0] > middle_wide and robot[1] > middle_tall:
        quadrants_count[3] += 1

sol1 = 1
for count in quadrants_count:
    sol1 *= count
print("Sol1:", sol1)

for seconds in range(0, 1000000):
    final_positions = []
    for line in ll:
        pos, vel = line.split(" v=")
        pos = pos.split("p=")[1]
        
        pos = tuple(map(int, pos.split(",")))
        vel = tuple(map(int, vel.split(",")))
        
        pos_x = (pos[0] + vel[0] * seconds)
        pos_y = (pos[1] + vel[1] * seconds)
        
        positions = [pos_x, pos_y]
        for i in range(len(positions)):
            to_divide = wide if i == 0 else tall
            if positions[i] < 0:
                positions[i] = (positions[i] % to_divide)
            else:
                positions[i] = (positions[i] % to_divide)

        final_positions.append(positions)
    
    
    tree = np.zeros((wide, tall))
    # print(f"Second {seconds + 1}")
    for position in final_positions:
        tree[position[0], position[1]] = 1
    
    v = False
    h = False
    for i in range(wide):
        if sum(tree[i, :]) > 30:
            v = True
            break
    
    for j in range(tall):
        if sum(tree[:, j]) > 30:
            h = True
            break
    
    if v and h:
        print(seconds)
        plt.imshow(tree)
        plt.show()
    

    