data = open("../data/day01.in").read().strip().split("\n\n")
l = [sum(list(map(lambda x: int(x), elf.split("\n")))) for elf in data]
print("Sol 1:", max(l))
print("Sol 2:", sum(sorted(l)[-3:]))