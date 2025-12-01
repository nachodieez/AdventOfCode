fn main() {
    println!("part1!");
    let input = include_str!("day1.in");
    let output = part2(input);
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

fn part2(input: &str) -> u32 {
    let mut start: i32 = 50;
    let mut times_zero = 0;
    for line in input.lines() {
        let (direction, times) = line.split_at(1);
        let times_int = times.trim().parse::<i32>().unwrap();

        for _ in 0..times_int {
            if direction == "L" {
                start -= 1;
            } else {
                start += 1;
            }
            // ugly but equivalent to start < 0 --> start := 100 - start in the 1-step case
            if start == -1 {
                start = 99;
            } else if start == 100 {
                start = 0;
            }

            times_zero += u32::from(start == 0);
        }
    }

    times_zero
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn test_part2() {
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

        let result_part_2 = 6;

        assert_eq!(part2(&input), result_part_2);
    }
}
