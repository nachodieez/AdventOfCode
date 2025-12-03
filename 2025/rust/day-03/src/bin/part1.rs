fn main() {
    println!("part1!");
    let input = include_str!("day3.in");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> u32 {
    let mut result = 0;

    for battery in input.lines() {
        // the number is 'ab'
        let chars: Vec<char> = battery.chars().collect();
        let mut a: u32 = chars[0].to_digit(10).unwrap();
        let mut b: u32 = chars[1].to_digit(10).unwrap();

        if b > a {
            a = b;
            b = 1;
        }

        let battery_length = battery.len();

        for (i, char) in (&chars[2..]).iter().enumerate() {
            // the end of the battery
            let char: u32 = char.to_digit(10).unwrap();

            if i == (battery_length - 3) {
                if char > b {
                    b = char;
                }

                break;
            }

            if char > a {
                a = char;
                b = 1;
            } else if char > b {
                b = char;
            }
        }

        let battery_joltage: u32 = (a.to_string() + &b.to_string()).parse().unwrap();
        result += battery_joltage;
    }

    result
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_one() {
        let input = "\
987654321111111
811111111111119
234234234234278
818181911112111";

        let result = 357;

        assert_eq!(part1(&input), result);
    }
}
