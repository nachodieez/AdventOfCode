import numpy as np

with open("../inputs/day12.txt") as f:
    ll = np.array([list(x.strip()) for x in f.readlines()])



letters = np.unique(ll)

prices = []
for letter in letters:
    price = 0
    locs = list(zip(*np.where(ll == letter)))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for loc in locs:
        for d in dirs:
            try: 
                coords = loc + np.array(d)
                adj = ll[coords[0], coords[1]]
                if adj != letter or any(np.array(coords) < 0): 
                    price += 1 
            except IndexError:
                price += 1
    prices.append(price * len(locs))
    print(letter)
    print(price * len(locs))
                
print("Sol 1:",sum(prices))