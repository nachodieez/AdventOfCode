fn main() {
    println!("part2!");
    let input = include_str!("day2.in");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> u64 {
    let id_ranges: String = input.lines().collect::<String>();
    let ranges = id_ranges.split(",");
    let mut sol = 0;
    for range in ranges {
        let parts: Vec<&str> = range.split("-").collect();

        let a: u64 = parts[0].parse().unwrap();
        let b: u64 = parts[1].parse().unwrap();

        for i in a..=b {
            // "repeated at least twice" --> single digit numbers are not valid
            if i < 11 {
                continue;
            };

            let i_str = i.to_string();
            let i_n_digits = i_str.len();

            let range_stop = if i_n_digits % 2 == 0 {
                i_n_digits / 2
            } else {
                (i_n_digits + 1) / 2
            };

            for k in 1..=range_stop {
                if i_n_digits % k != 0 {
                    continue;
                }

                if i_str == (&i_str[0..k].repeat(i_n_digits / k)).to_string() {
                    sol += i;
                    break;
                }
            }
        }
    }

    sol
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_two() {
        let input = "\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124";
        let result = 4174379265;

        assert_eq!(part2(&input), result);
    }
}
