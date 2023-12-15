from collections import OrderedDict

with open("../data/day15.in") as f:
    data = f.read().strip().split(",")

def myhash(string):
    res = 0
    for letter in string:
        res += ord(letter)
        res *= 17
        res %= 256
    return res

print("Sol 1", sum(myhash(sequence) for sequence in data))

boxes = [OrderedDict() for _ in range(256)]

# s stands for sequence
for s in data:
    if "-" in s:
        label = s[:s.find("-")]
        box = myhash(label)
        if label in boxes[box]:
            del boxes[box][label]
    elif "=" in s:
        label = s[:s.find("=")]
        box = myhash(label)
        focal_length = int(s[s.find("=") + 1:])
        boxes[box][label] = focal_length

sol2 = 0
for nbox, box in enumerate(boxes):
    for nslot, focal_length in enumerate(box.values()):
        sol2 += (nbox + 1) * (nslot + 1) * focal_length
print("Sol 2:", sol2)