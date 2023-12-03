import re
from itertools import chain

data = open("../data/day03.in").read().strip().split("\n")

# part 1
symbols_it = []
for line in data:
    symbols_indices = set([m.start() for m in re.finditer(r"[+@*$&\-=/%#]", line)])
    symbols_it.append(symbols_indices)

valid_numbers = []
for it, line in enumerate(data):
    prev_line = max(0, it - 1)
    pos_line = min(len(data) - 1 , it + 1)
    symbols_lines = set.union(*symbols_it[prev_line:(pos_line + 1)])
    numbers = set(re.findall(r"\d+", line))
    for number in numbers:
        number_indices = list([m.start() for m in re.finditer(number, line)])
        for index in number_indices:
            prev = max(index - 1, 0)
            pos = index + len(number)
            if (line[prev:pos].isdigit() and prev != 0) or (line[index:(pos + 1)].isdigit() and pos != len(line)):
                continue
            span = set(range(prev, pos + 1))
            if len(span & symbols_lines):
                valid_numbers.append(int(number))
print("Sol 1:", sum(valid_numbers))

# part 2
gears_it = []
for i, line in enumerate(data):
    gears_indices = set([m.start() for m in re.finditer(r"\*", line)])
    gears_it.append(gears_indices)

numbers_adjacent_gear = []
for it, line in enumerate(data):
    list_it = []
    prev_line = max(0, it - 1)
    pos_line = min(len(data) - 1 , it + 1)
    gears_lines = set.union(*gears_it[prev_line:(pos_line + 1)])
    numbers = set(re.findall(r"\d+", line))
    for number in numbers:
        number_indices = list([m.start() for m in re.finditer(number, line)])
        for index in number_indices:
            prev = max(index - 1, 0)
            pos = index + len(number)
            if (line[prev:pos].isdigit() and prev != 0) or (line[index:(pos + 1)].isdigit() and pos != len(line)):
                continue
            span = set(range(prev, pos + 1))
            for li in range(prev_line, pos_line + 1):
                gears_current_line = gears_it[li]
                if len(span & gears_current_line):
                    for gear in (span & gears_current_line):
                        list_it.append((int(number), (li, gear))) # line, pos
    numbers_adjacent_gear.append(list_it)

numbers_adjacent_gear = list(filter(None, numbers_adjacent_gear)) # empty list evaluate to False
numbers_adjacent_gear = list(chain.from_iterable(numbers_adjacent_gear))
print(numbers_adjacent_gear)

sol2 = 0
for i in range(len(numbers_adjacent_gear)):
    for j in range(i + 1, len(numbers_adjacent_gear)):
        if numbers_adjacent_gear[i][1] == numbers_adjacent_gear[j][1]:
            sol2 += numbers_adjacent_gear[i][0] * numbers_adjacent_gear[j][0]
print("Sol 2:", sol2)