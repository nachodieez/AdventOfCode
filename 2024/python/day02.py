import numpy as np


ll = [line.strip() for line in open("../inputs/day02.txt").readlines()]

# Part 1
valid = 0
for line in ll:
    line = np.array(line.split(" "), dtype=np.int32)

    diffs = np.diff(line)

    first = np.all(diffs > 0) | np.all(diffs < 0)
    second = np.all((np.abs(diffs) >= 1) & (np.abs(diffs) <= 3))
    
    valid += first & second
    
print("Sol 1: ", valid)

# Part 2
valid = 0
for line in ll:
    line = np.array(line.split(" "), dtype=np.int32)
    for el in range(len(line)):
        nline = np.delete(line, el)

        diffs = np.diff(nline)

        first = np.all(diffs > 0) | np.all(diffs < 0)
        second = np.all((np.abs(diffs) >= 1) & (np.abs(diffs) <= 3))
        
        if first & second:
            valid += 1
            break    
           
print("Sol 2:", valid)