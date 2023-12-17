import numpy as np

with open("../data/day16.in") as f:
    grid = np.array([list(x) for x in f.read().strip().split("\n")])
# note how to "\" is stored as "\\"

class Beam:
    def __init__(self, position: tuple, direction: str) -> None:
        self.i, self.j = position
        self.direction = direction
        self.can_move = True

        # current tile
        self.tile = grid[self.i, self.j]

        # the initialization tile is energized
        energized_tiles[self.i, self.j] = 1

        self.update_direction()

        self.update_state()

    def get_direction(self) -> str:
        return self.direction
    
    def get_position(self) -> tuple:
        return (self.i, self.j)

    def energize_tile(self):
        energized_tiles[self.i, self.j] = 1

    def get_state(self) -> tuple:
        return (self.get_position(), self.get_direction())
    
    def update_state(self) -> None:
        states[self.get_state()] = 1

    def update_direction(self) -> None:
        if self.tile == ".":
            pass
        elif self.tile == "/":
            if self.direction == "up":
                self.direction = "right"
            elif self.direction == "down":
                self.direction = "left"
            elif self.direction == "right":
                self.direction = "up"
            elif self.direction == "left":
                self.direction = "down"
        elif self.tile == "\\":
            if self.direction == "up":
                self.direction = "left"
            elif self.direction == "down":
                self.direction = "right"
            elif self.direction == "right":
                self.direction = "down"
            elif self.direction == "left":
                self.direction = "up"
        elif self.tile == "|":
            if self.direction == "up":
                pass
            elif self.direction == "down":
                pass
            elif self.direction == "right":
                self.direction = "up"
                beams.append(Beam(position=(self.i, self.j), direction="down"))
            elif self.direction == "left":
                self.direction = "up"
                beams.append(Beam(position=(self.i, self.j), direction="down"))
        elif self.tile == "-":
            if self.direction == "up":
                self.direction = "right"
                beams.append(Beam(position=(self.i, self.j), direction="left"))
            elif self.direction == "down":
                self.direction = "right"
                beams.append(Beam(position=(self.i, self.j), direction="left"))
            elif self.direction == "right":
                pass
            elif self.direction == "left":
                pass

    def move(self) -> None:
        if self.direction == "up":
            self.i -= 1
        elif self.direction == "down":
            self.i += 1
        elif self.direction == "right":
            self.j += 1
        elif self.direction == "left":
            self.j -= 1  
        
        if self.i < 0 or self.i >= grid.shape[0] or self.j < 0 or self.j >= grid.shape[1]:
            self.can_move = False
            return
        # I need to avoid infinite loops, thus I keep track of the different states
        if self.get_state() in states:
            self.can_move = False
            return
        
        self.tile = grid[self.i, self.j]
        self.energize_tile()
        self.update_state()

        self.update_direction()

    
    def can_it_move(self) -> bool:
        return self.can_move
            

    def __repr__(self) -> str:
        return f"Beam({self.i, self.j}, {self.direction})"


# create a np array to keep track of the energized tile
energized_tiles = np.zeros(grid.shape, dtype=np.int8)
beams = []
states = {}
beams.append(Beam(position=(0,0), direction="right"))

for beam in beams:
    while beam.can_it_move():
        beam.move() 

print("Sol 1:", np.sum(energized_tiles))

canonical_beams = []
for j in range(grid.shape[0]):
    canonical_beams.append([Beam(position=(0,j), direction="down")])
    canonical_beams.append([Beam(position=(grid.shape[0]-1,j), direction="up")])

for i in range(grid.shape[1]):
    canonical_beams.append([Beam(position=(i,0), direction="right")])
    canonical_beams.append([Beam(position=(i,grid.shape[1]-1), direction="left")])

sol2 = -1
for iter in canonical_beams:
    beams = iter
    energized_tiles = np.zeros(grid.shape, dtype=np.int8)
    states = {} 
    for beam in beams:
        while beam.can_it_move():
            beam.move() 
    sol2 = max(sol2, np.sum(energized_tiles))

print("Sol 2:", sol2)