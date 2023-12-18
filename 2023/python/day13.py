import numpy as np
data = open("../data/day13.in").read().strip().split("\n\n")

def get_reflections(pattern, part1 = True):
    res = 0
    pattern = np.array([list(x) for x in pattern.split("\n")])
    rows, cols = pattern.shape
    for row in range(rows):
        first = pattern[:row,:][::-1,:]
        second = pattern[row:,:]
        m = min(first.shape[0], second.shape[0])
        first = first[:m, :]
        second = second[:m, :]
        if part1:
            if np.all([first[i,:] == second[i,:] for i in range(m)]):
                res += row * 100
        else:
            if np.count_nonzero([first[i,:] != second[i,:] for i in range(m)]) == 1:
                res += row * 100
    
    for col in range(cols):
        first = pattern[:,:col][:,::-1]
        second = pattern[:,col:]
        m = min(first.shape[1], second.shape[1])
        first = first[:,:m]
        second = second[:,:m]
        if part1:
            if np.all([first[:,i] == second[:,i] for i in range(m)]):
                res += col
        else:
            if np.count_nonzero([first[:,i] != second[:,i] for i in range(m)]) == 1:
                res += col

    return res

print("Sol 1:", sum(get_reflections(pattern) for pattern in data))
print("Sol 2:", sum(get_reflections(pattern, part1=False) for pattern in data))