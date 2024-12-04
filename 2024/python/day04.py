import regex as re
import numpy as np


ll = [x.strip() for x in open("../inputs/day04.txt").readlines()]

# Part 1
rll = [''.join(list(x)) for x in zip(*ll)]
ll2d = np.array([list(x) for x in ll])
a = ll2d

# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))  
diags = [''.join(n.tolist()) for n in diags]

pattern = r"XMAS|SAMX"
sol1 = 0
for line in ll:
    sol1 += len(re.findall(pattern, line, overlapped=True))

for line in rll:
    sol1 += len(re.findall(pattern, line, overlapped=True))

for line in diags:
    sol1 += len(re.findall(pattern, line, overlapped=True))
print("Sol1:", sol1)

# Part 2
n, m  = ll2d.shape
sol2 = 0
pattern2 = ("MAS", "SAM")
for i in range(n-2):
    for j in range(m-2):
        data = ll2d[i:i+3, j:j+3]
        diag = ''.join(np.diag(data))
        other_diag = ''.join(np.diag(np.fliplr(data)))
        if diag in pattern2 and other_diag in pattern2:
            sol2 += 1
print("Sol2:", sol2)
        
        
