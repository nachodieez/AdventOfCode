import numpy as np
import copy

data = open("../data/day11.in").read().strip().split("\n")

lines = np.array([list(line) for line in data])
expanded_rows = []
expanded_columns = []
for row in range(lines.shape[0]):
    if "#" not in lines[row, :]:
        expanded_rows.append(row)

for column in range(lines.shape[1]):
    if "#" not in lines[:, column]:
        expanded_columns.append(column)

lines = np.insert(lines, expanded_rows, ".", axis = 0)
lines = np.insert(lines, expanded_columns, ".", axis = 1)

galaxies_coordinates = tuple(zip(*np.where(lines == "#")))

sol1 = 0
for i in range(len(galaxies_coordinates)):
    for j in range(i):
        sol1 += abs(galaxies_coordinates[i][0] - galaxies_coordinates[j][0]) + abs(galaxies_coordinates[i][1] - galaxies_coordinates[j][1])
print("Sol 1:", sol1)

lines = np.array([list(line) for line in data])
expanded_rows = []
expanded_columns = []
for row in range(lines.shape[0]):
    if "#" not in lines[row, :]:
        expanded_rows.append(row)

for column in range(lines.shape[1]):
    if "#" not in lines[:, column]:
        expanded_columns.append(column)

galaxies_coordinates = [list(a) for a in zip(*np.where(lines == "#"))]
for coordinates in range(len(galaxies_coordinates)):
    galaxies_coordinates_copy = copy.deepcopy(galaxies_coordinates)
    for row in expanded_rows:
        if galaxies_coordinates_copy[coordinates][0] > row:
            galaxies_coordinates[coordinates][0] += 999999
    for column in expanded_columns:
        if galaxies_coordinates_copy[coordinates][1] > column:
            galaxies_coordinates[coordinates][1] += 999999
sol2 = 0
for i in range(len(galaxies_coordinates)):
    for j in range(i):
        sol2 += abs(galaxies_coordinates[i][0] - galaxies_coordinates[j][0]) + abs(galaxies_coordinates[i][1] - galaxies_coordinates[j][1])
print("Sol 2:", sol2)