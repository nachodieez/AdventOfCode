data = open("../data/day04.in").read().strip().split("\n")

fully_contained = []
overlapping = []
for index, pair in enumerate(data):
    first, second = pair.split(",")
    first_initial, first_end = first.split("-")
    second_initial, second_end = second.split("-")
    first_set = set(range(int(first_initial), int(first_end) + 1))
    second_set = set(range(int(second_initial), int(second_end) + 1))
    set_union = first_set | second_set
    set_intersection = first_set & second_set
    if (first_set == set_union) or (second_set == set_union):
        fully_contained.append(index)
    if len(set_intersection):
        overlapping.append(index)
print("Sol 1:", len(fully_contained))
print("Sol 2:", len(overlapping))