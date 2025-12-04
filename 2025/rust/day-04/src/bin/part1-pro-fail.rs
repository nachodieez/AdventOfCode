fn main() {
    println!("part1!");
    let input = include_str!("day4.in");
    let output = part1(input);
    dbg!(output);
}

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

    fn accesible_rolls(&self, p: &Pos) -> i64 {
        match self.get(p) {
            Some('@') => {}
            _ => return 0,
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
            let mut curr = *p;
            loop {
                if let Some(next) = curr.step(dir, self.width, self.height) {
                    curr = next;

                    match self.get(&curr) {
                        Some('@') => {
                            count += 1;
                            break;
                        }

                        Some(_) => continue,
                        None => break,
                    }
                } else {
                    break;
                }
            }
        }
        count
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

fn part1(input: &str) -> u64 {
    let grid = Grid::from_str(input);

    let mut sol1 = 0;
    for x in 0..grid.width {
        for y in 0..grid.height {
            if grid.accesible_rolls(&Pos { x, y }) < 4 {
                sol1 += 1
            }
        }
    }

    sol1
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_one() {
        let result = 13;
        let input = "/
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.";

        assert_eq!(part1(&input), result);
    }
}
