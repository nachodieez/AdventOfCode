fn main() {
    println!("part2!");
    let input = include_str!("day4.in");
    let output = part2(input);
    dbg!(output);
}

#[derive(Debug)]
struct Grid {
    cells: Vec<Vec<char>>,
    width: i64,
    height: i64,
}

impl Grid {
    fn from_str(input: &str) -> Self {
        let cells: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();

        let height = cells.len() as i64;
        let width = cells.first().map(|row| row.len()).unwrap() as i64;

        Grid {
            cells,
            width,
            height,
        }
    }

    fn in_bounds(&self, p: &Pos) -> bool {
        p.y < self.height && p.x < self.width
    }

    fn get(&self, p: &Pos) -> Option<char> {
        if self.in_bounds(p) {
            Some(self.cells[p.y as usize][p.x as usize])
        } else {
            None
        }
    }

    fn accesible_rolls(&self, p: &Pos) -> Option<i64> {
        match self.get(p) {
            Some('@') => {}
            _ => return None,
        }

        let all_dirs = [
            Dir::Up,
            Dir::Down,
            Dir::Left,
            Dir::Right,
            Dir::UpLeft,
            Dir::UpRight,
            Dir::DownLeft,
            Dir::DownRight,
        ];

        let mut count = 0;
        for dir in all_dirs {
            let curr = match p.step(dir, self.width, self.height) {
                Some(Pos { x, y }) => Pos { x, y },
                None => continue,
            };
            match self.get(&curr) {
                Some('@') => {
                    count += 1;
                }

                Some(_) => continue,
                None => continue,
            }
        }
        Some(count)
    }

    fn remove_rolls(self, to_remove: Vec<Pos>) -> Self {
        let mut current_cells = self.cells;
        for pos in to_remove {
            current_cells[pos.y as usize][pos.x as usize] = '.';
        }

        Grid {
            cells: current_cells,
            ..self
        }
    }
}

#[derive(Copy, Clone, Debug)]
struct Pos {
    x: i64,
    y: i64, // I know that they cannot be negative but easier for adding deltas
}

#[derive(Copy, Clone, Debug)]
enum Dir {
    Up,
    Down,
    Left,
    Right,
    UpLeft,
    UpRight,
    DownLeft,
    DownRight,
}

impl Pos {
    fn step(self, dir: Dir, width: i64, height: i64) -> Option<Pos> {
        let (dx, dy) = dir.delta();

        let nx = self.x + dx;
        let ny = self.y + dy;

        if (nx < 0 || ny < 0) || (nx >= width || ny >= height) {
            None
        } else {
            Some(Pos { x: nx, y: ny })
        }
    }
}

impl Dir {
    fn delta(self) -> (i64, i64) {
        match self {
            Dir::Up => (0, -1),
            Dir::Down => (0, 1),
            Dir::Left => (-1, 0),
            Dir::Right => (1, 0),
            Dir::UpLeft => (-1, -1),
            Dir::UpRight => (1, -1),
            Dir::DownLeft => (-1, 1),
            Dir::DownRight => (1, 1),
        }
    }
}

fn part2(input: &str) -> u64 {
    let mut grid = Grid::from_str(input);

    let mut sol2 = 0;
    loop {
        let mut changes_iter = 0;
        let mut to_remove: Vec<Pos> = Vec::new();
        for x in 0..grid.width {
            for y in 0..grid.height {
                let pos_to_check = Pos { x, y };
                match grid.accesible_rolls(&pos_to_check) {
                    Some(n) => {
                        if n < 4 {
                            sol2 += 1;
                            changes_iter += 1;
                            to_remove.push(pos_to_check);
                        }
                    }
                    None => continue,
                };
            }
        }

        if changes_iter == 0 {
            break;
        }

        grid = grid.remove_rolls(to_remove);
    }

    sol2
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_two() {
        let result = 43;
        let input = "..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.";

        assert_eq!(part2(&input), result);
    }
}
