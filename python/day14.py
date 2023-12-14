import numpy as np

with open("../data/day14.in") as f:
    ll = np.array([list(x.strip()) for x in f.readlines()])

def move_north(positions):
    rows, columns = positions.shape
    new_positions = positions.copy()
    for i in range(rows):
        for j in range(columns):
            for upper in reversed(range(1,i+1)):
                if new_positions[upper-1,j] == "." and new_positions[upper,j] == "O":
                    new_positions[upper,j] = "."
                    new_positions[upper-1,j] = "O"
    
    return new_positions

sol1 = 0
ll2 = move_north(ll)[::-1,:]
for i in range(ll2.shape[0]):
    sol1 += np.sum(ll2[i,:] == "O") * (i+1)
print("Sol 1:", sol1)

def simply_move(positions):
    rows, columns = positions.shape
    new_positions = positions.copy()

    # north
    for i in range(rows):
        for j in range(columns):
            for upper in reversed(range(1,i+1)):
                if new_positions[upper-1,j] == "." and new_positions[upper,j] == "O":
                    new_positions[upper,j] = "."
                    new_positions[upper-1,j] = "O"
    # west
    for i in range(rows):
        for j in range(columns):
            for left in range(1,columns):
                if new_positions[i,left-1] == "." and new_positions[i,left] == "O":
                    new_positions[i,left] = "."
                    new_positions[i,left-1] = "O"

    # south
    for i in reversed(range(rows)):
        for j in range(columns):
            for lower in range(rows-1):
                if new_positions[lower+1,j] == "." and new_positions[lower,j] == "O":
                    new_positions[lower+1,j] = "O"
                    new_positions[lower,j] = "."
    # east
    for i in range(rows):
        for j in range(columns):
            for right in reversed(range(columns-1)):
                if new_positions[i,right] == "O" and new_positions[i,right+1] == ".":
                    new_positions[i,right] = "."
                    new_positions[i,right+1] = "O"
    
    return new_positions

d = dict()
d[1] = simply_move(ll)
cycle = -1
for i in range(2,10000):
    if i % 10 == 0:
        print("it", i)
    d[i] = simply_move(d[i-1])
    for j in range(1, i-1):
        if np.all(d[i] == d[j]):
            cycle = i - j # cycle length
            cycle_start = j # it where we enter the cycle
            break
    if cycle != -1:
        break

# cycle starts at it cycle_start every cycle iterations so 
# d[cycle_start + x] == d[cycle_start + x + (n * cycle)]

sol2 = 0
ll3 = d[cycle_start + (1_000_000_000 - cycle_start) % cycle][::-1,:]
for i in range(ll3.shape[0]):
    sol2 += np.sum(ll3[i,:] == "O") * (i+1)
print("Sol 2:", sol2)