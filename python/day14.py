import numpy as np

with open("../data/day14.in") as f:
    ll = np.array([list(x.strip()) for x in f.readlines()])

def move_north(positions):
    rows, columns = positions.shape
    new_positions = positions.copy()
    for i in range(1,rows):
        for j in range(columns):
            if new_positions[i,j] == "O":
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