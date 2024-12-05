from collections import defaultdict

with open("../inputs/day05.txt") as f:
    ll = f.read().splitlines()


# Part 1
cut = ll.index("")
ordering = ll[:cut]
updates = ll[cut + 1 :]

ordering = list(map(lambda x: x.split("|"), ordering))
rules = defaultdict(list)

for tup in ordering:
    X, Y = tup
    rules[int(X)].append(int(Y))


def is_valid(numbers):
    n_numbers = len(numbers)
    if n_numbers == 1:
        return numbers

    valid = True
    incorrect = None
    for i in range(n_numbers):
        key = numbers[i]
        for j in range(i + 1, n_numbers):
            if numbers[j] not in rules[key]:
                valid = False
                incorrect = numbers[j]
                break
        if not valid:
            break
    return valid


middles = []
not_valids = []
for update in updates:
    numbers = update.split(",")
    numbers = [int(x) for x in numbers]
    valid = is_valid(numbers)
    if valid:
        middles.append(numbers[(len(numbers) // 2)])
    else:
        not_valids.append(numbers)

print("Sol1:", sum(middles))


# Part 2
def order(L, el):
    if L is None:
        return [el]

    for i in range(len(L)):
        new = L[:i] + [el] + L[i:]
        valid = is_valid(new)
        if valid:
            return new
    return L + [el]


corrected_middles = []
for i in range(len(not_valids)):
    not_valid = not_valids[i]
    valid = []
    while not_valid:
        el = not_valid.pop()
        valid = order(valid, el)
    corrected_middles.append(valid[(len(valid) // 2)])

print("Sol2:", sum(corrected_middles))
