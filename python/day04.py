import re

data = open("../data/day04.in").read().strip().split("\n")

points = 0
for card in data:
    lists = card.split(":")[1]
    sets = []
    for numbers in lists.split("|"):
        s = []
        for number in numbers.split(" "):
            if number.isdigit():
                s.append(int(number))
        sets.append(set(s))
    winning = len(set.intersection(*sets))
    if winning > 0:
        points += 2**(winning - 1)
print("Sol 1:", points)

sol2 = len(data)
for card in data:
    lists = card.split(":")[1]
    card_index = int(re.findall(r'\d+', card)[0]) - 1
    sets = []
    for numbers in lists.split("|"):
        s = []
        for number in numbers.split(" "):
            if number.isdigit():
                s.append(int(number))
        sets.append(set(s))
    winning = len(set.intersection(*sets))
    sol2 += winning
    if len(data[card_index:card_index+winning+1]):
        for d in data[card_index+1:card_index+winning+1]:
            data.append(d)
print("Sol 2:", sol2)