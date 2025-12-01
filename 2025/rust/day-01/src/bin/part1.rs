fn main() {
    println!("part1!");
    let input = include_str!("day1.in");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> u32 {
    let mut start: i32 = 50;
    let mut times_zero = 0;
    for line in input.lines() {
        let (direction, times) = line.split_at(1);
        let times_int = times.trim().parse::<i32>().unwrap();

        if direction == "L" {
            start -= times_int;
        } else {
            start += times_int;
        }

        if start.abs() % 100 == 0 {
            times_zero += 1;
        }
    }

    times_zero
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_one() {
        let input = "\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82";

        let result = 3;

        assert_eq!(part1(&input), result);
    }
}
