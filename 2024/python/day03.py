import re

with open("../inputs/day03.txt") as f:
    l = f.read().strip()

# Part 1
def compute(l):
    sol = 0
    tuples = re.findall(r"mul\((\d+),(\d+)\)", l)
    for numbers in tuples:
        X, Y = numbers
        sol += int(X) * int(Y)
    return sol
print("Sol1:", compute(l))


# Part 2
pattern = r"do\(\)|don't\(\)"
matches = [(match.group(), match.end()) for match in re.finditer(pattern, l)]

dos = []
enabled = True
prev = 0
for t in matches:
    if enabled: 
        dos.append((prev, int(t[1])))
    prev = t[1]
    enabled = t[0] == "do()"
    
if enabled:
    dos.append((prev, len(l)))

input_converted = ""
for t in dos:
    input_converted += l[t[0]:t[1]]    
print("Sol2:", compute(input_converted))