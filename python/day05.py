import re

data = open("../data/day05.in").read().strip().split("\n\n")

current = list(map(int, re.findall(r"\d+", data[0]))) # seeds

for mapping in data[1:]:
    for i in range(len(current)):
        for line in mapping.split("\n")[1:]:
            destination_start, source_start, range_length = list(map(int, re.findall(r"\d+", line)))
            if source_start <= current[i] < (source_start + range_length):
                current[i] = destination_start + (current[i] - source_start)
                break
print("Sol:", min(current))    

seeds = list(map(int, re.findall(r"\d+", data[0])))

for location in range(100000000000):
    solved = False
    current_source = location
    for mapping in list(reversed(data[1:])):
        for line in reversed(mapping.split("\n")[1:]):
            destination_start, source_start, range_length = list(map(int, re.findall(r"\d+", line)))
            if destination_start <= current_source < (destination_start + range_length):
                current_source = source_start + (current_source - destination_start)
                break
    for i in range(int(len(seeds)/2)):
        if seeds[i*2] <= current_source < seeds[i*2] + seeds[i*2+1]:
            solved = True
            print("Sol2:", location)
    if solved:
        break