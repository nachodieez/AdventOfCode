data = open("../data/day02.in").read().strip().split("\n")

scores = {
    "AX" : 4, "AY" : 8, "AZ" : 3,
    "BX" : 1, "BY" : 5, "BZ" : 9,
    "CX" : 7, "CY" : 2, "CZ" : 6
}

l = [scores[game.replace(" ", "")] for game in data]
print("Sol 1:", sum(l)) 

scores2 = {
    "AX" : 3, "AY" : 4, "AZ" : 8,
    "BX" : 1, "BY" : 5, "BZ" : 9,
    "CX" : 2, "CY" : 6, "CZ" : 7
}

l2 = [scores2[game.replace(" ", "")] for game in data]
print("Sol 1:", sum(l2)) 