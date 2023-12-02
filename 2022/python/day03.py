import string

data = open("../data/day03.in").read().strip().split("\n")

alphabet = string.ascii_lowercase + string.ascii_uppercase
scores = dict(zip(alphabet, list(range(1, 53))))

items = []
for rucksack in data:
    first = set(rucksack[:int(len(rucksack) / 2)])
    second = set(rucksack[int(len(rucksack) / 2):])
    items.append(list(first & second)[0])
print("Sol 1:", sum([scores[item] for item in items]))

items2 = []
rucksacks = []
counter = 1
for rucksack in data:
    rucksacks.append(set(rucksack))
    if counter % 3 == 0:
        items2.append(list(set.intersection(*rucksacks))[0])
        rucksacks = []
    counter += 1
print("Sol 2:", sum([scores[item] for item in items2]))