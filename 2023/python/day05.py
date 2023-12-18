import re

data = open("../data/day05.in").read().strip().split("\n\n")

current = list(map(int, re.findall(r"\d+", data[0]))) # seeds

def get_location(s):
    res = s
    for mapping in data[1:]:
        for line in mapping.split("\n")[1:]:
            destination_start, source_start, range_length = list(map(int, re.findall(r"\d+", line)))
            if source_start <= res < (source_start + range_length):
                res = destination_start + (res - source_start)
                break
    return res

for i in range(len(current)):
    current[i] = get_location(current[i])
print("Sol:", min(current))

def f(input, mapping):
    # input:   [x,y) (i.e. [x, y-1])
    # mapping: [a,b) -> [c,d)
    # output: all the mapped intervals for the values inside input
    
    x, y = input
    mapping = sorted(mapping, key=lambda x: x[0][0])

    # If the end of the input interval is smaller than the start of the first interval
    # of the ordered mapping, return the interval itself
    if y - 1 < mapping[0][0][0]:
        return [(x, y)]
    
    new_ranges = []
    prev_map = mapping[0]

    for map in mapping:
        b_prev = prev_map[0][1]
        a, b = map[0]
        c, d = map[1]

        # If there is a gap between two intervals, map the numbers of the input
        # to themselves. b_prev is not included so, if you have (10,20) and (20,30)
        # the element 20 is only mapped in the second interval but only if x is
        # between those values.
        if b_prev < x <= a:
            # If y is bigger than the end of the interval, set it as the end of the
            # interval and break the loop, as no more mapping is needed.
            if y > x + (a - b_prev):
                new_ranges.append((x, y))
                x = y
                break
            else:
                new_ranges.append((x, x + (a - b_prev)))
                x += (a - b_prev)
        
        # The input interval is fully contained in the mapping interval.
        # All values of the interval should be mapped.
        elif a <= x <= y <= b:
            new_ranges.append((c + (x-a), c + (x-a) + (y - x)))
            x += (x-a) + (y - (x + (x-a)))
        
        # The input interval is partially contained in the mapping interval.
        # Only values from x to (b-1) should be mapped generating the new
        # interval [c + (x-a), d)
        elif a <= x <= b - 1 < y - 1:
            new_ranges.append((c + (x-a), d))
            x += (d - (c + (x-a)))
        
        # If we mapped are the values on the interval, break
        if x == y:
            break    

        prev_map = map

    # If there are no maps left but some values are yet to be mapped, map them
    if y - x > 0:
        new_ranges.append((x, y))
    
    return new_ranges

seeds = list(map(int, re.findall(r"\d+", data[0])))

ranges = [(seeds[i*2], seeds[i*2] + seeds[i*2+1]) for i in range(int(len(seeds) / 2))]
for chunk in data[1:]:
    mappings = []
    for line in chunk.split("\n")[1:]:
        destination_start, source_start, range_length = list(map(int, re.findall(r"\d+", line)))
        mappings.append(
            [(source_start, source_start + range_length),
             (destination_start, destination_start + range_length)])
    new_ranges = []
    for r in ranges:
        for new_r in f(r, mappings):
            new_ranges.append(new_r)
    ranges = new_ranges
print("Sol 2:", sorted(ranges)[0][0])

# seeds = list(map(int, re.findall(r"\d+", data[0]))) # seeds
# seeds = [list(range(seeds[i*2], seeds[i*2] + seeds[i*2+1])) for i in range(int(len(seeds) / 2))]
# seeds = list(chain.from_iterable(seeds))
# for i in range(len(seeds)):
#     seeds[i] = get_location(seeds[i])
# print("Min:", min(seeds))


# seeds = list(map(int, re.findall(r"\d+", data[0]))) # seeds
# seeds = [(seeds[i*2], seeds[i*2] + seeds[i*2+1]) for i in range(int(len(seeds) / 2))]
# seeds = list(chain.from_iterable(seeds))
# mapped_seeds = [get_location(seed) for seed in seeds]
# argmin = np.argmin(mapped_seeds)
# m = min(mapped_seeds)
# if argmin % 2 == 0:
#     r = range(seeds[argmin],seeds[argmin+1])
# else:
#     r = range(seeds[argmin-1], seeds[argmin])
# for seed in r:
#     m = min(m, get_location(seed))
# print("Sol 2:", m)

# maps = []

# for mapping in data[1:]:
#     m = []
#     for line in mapping.split("\n")[1:]:
#         destination_start, source_start, range_length = list(map(int, re.findall(r"\d+", line)))
#         d = {(source_start, source_start + range_length) : (destination_start, destination_start + range_length)}
#         m.append(d)
#     maps.append(m)

# def compare_intervals(interval1, interval2):
#     """empiza a no tener ningún tipo de sentido"""
#     a,b = interval1
#     c,d = interval2
#     if c < a and d < b:
#         print((a, d), (d + 1, b))
#     if c > a and d > b:
#         print((c, b), (a, c-1), (b+1, d))
# compare_intervals((79, 93), (75, 83))
# compare_intervals((79, 93), (85, 100))

# d = list(map(int, re.findall(r"\d+", data[0])))
# seeds = [d[i*2] for i in range(int(len(d)/2))]
# range_lengths = [d[i*2+1] for i in range(int(len(d)/2))]
# m = [max(current) for _ in seeds]
# i = 0
# for seed, range_length in zip(seeds, range_lengths):
#     s = seed
#     r = range_length
#     a, b = s, s + r 
#     while r > 1:
#         r = ceil(r / 2)
#         la = get_location(a)
#         lb = get_location(b)
#         if la < lb:
#             m[i] = la
#             b -= r
#         else:
#             m[i] = lb
#             a += r
#     i += 1
# print(m)
    

# current_copy = current.copy()
# while True:
#     argmin = np.argmin(current_copy)
#     if argmin % 2 == 0:
#         break
#     current_copy[argmin] = max(current_copy)

# range_len = current[argmin+1]
# for i in range(ceil(log2(current[argmin+1]))):
#     new_m = min(m, get_location(current[argmin] + range_len))
#     range_len = ceil(range_len/2)
#     print(range_len)
# print(m)

# seeds = list(map(int, re.findall(r"\d+", data[0])))

# for location in range(1000000000):
#     print(location)
#     solved = False
#     current_source = location
#     for mapping in list(reversed(data[1:])):
#         for line in reversed(mapping.split("\n")[1:]):
#             destination_start, source_start, range_length = list(map(int, re.findall(r"\d+", line)))
#             if destination_start <= current_source < (destination_start + range_length):
#                 current_source = source_start + (current_source - destination_start)
#                 break
#     for i in range(int(len(seeds)/2)):
#         if seeds[i*2] <= current_source < seeds[i*2] + seeds[i*2+1]:
#             solved = True
#             print("Sol2:", location)
#     if solved:
#         break