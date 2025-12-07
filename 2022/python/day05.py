import re
from collections import deque


with open("day05.in", mode="r") as f:
    data = f.readlines()

find_numbers = re.compile(r"\d+")
line_with_pos = 0
lines_with_crates = 0
for i, line in enumerate(data):
    try:
        int(line.replace(" ", ""))
        line_with_pos = i
        break
    except:
        lines_with_crates += 1
        pass

columns = [int(x) - 1 for x in find_numbers.findall(data[line_with_pos])]

stacks = [deque() for _ in range(len(columns))]
for index_line in range(lines_with_crates):
    l = []
    for i in columns:
        char = data[index_line][1 + i*4]
        if char != ' ':
            stacks[i].append(char)


move = []
fro = []  # from
to = []
for order_line in data[(lines_with_crates + 2):]:
    numbers = find_numbers.findall(order_line)
    move.append(int(numbers[0]))
    fro.append(int(numbers[1]))
    to.append(int(numbers[2]))


steps = len(move)

# for step in range(steps):
#     from_stack = stacks[fro[step]-1]
#     to_stack = stacks[to[step]-1]
#
#     for _ in range(move[step]):
#         moved_thing = from_stack.popleft()
#         to_stack.extendleft(moved_thing)
#
# sol1 = ''.join([x[0] for x in stacks])
# print(sol1)

for step in range(steps):
    from_stack = stacks[fro[step]-1]
    to_stack = stacks[to[step]-1]
    
    to_move = []
    for _ in range(move[step]):
        to_move.append(from_stack.popleft())

    to_stack.extendleft(to_move[::-1])

sol2 = ''.join([x[0] for x in stacks])
print(sol2)

