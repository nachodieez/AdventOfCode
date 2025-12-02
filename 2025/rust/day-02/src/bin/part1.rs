fn main() {
    println!("part1!");
    let input = include_str!("day2.in");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> u64 {
    let id_ranges: String = input.lines().collect::<String>();
    let ranges = id_ranges.split(",");
    let mut sol = 0;
    for range in ranges {
        let parts: Vec<&str> = range.split("-").collect();
        println!("{}", range);
        let a: u64 = parts[0].parse().unwrap();
        let b: u64 = parts[1].parse().unwrap();

        for i in a..=b {
            let i_str = i.to_string();
            let i_n_digits = i_str.len();

            if i_n_digits % 2 != 0 {
                continue;
            }

            let (first_half, second_half) = i_str.split_at(i_n_digits / 2);

            if first_half == second_half {
                sol += i;
            }
        }
    }

    sol
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_one() {
        let input = "\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124";
        let result = 1227775554;

        assert_eq!(part1(&input), result);
    }
}
