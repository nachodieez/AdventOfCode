fn main() {
    println!("part2!");
    let input = include_str!("day3.in");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> u64 {
    let mut result = 0;

    for battery in input.lines() {
        // the number is 'ab'
        let battery_length = battery.len();
        let mut prev_max_index = 0;
        let mut battery_joltage = "".to_string();
        for position in 0..12 {
            let starting_point = if prev_max_index != 0 {
                position.max(prev_max_index + 1)
            } else {
                position
            };

            let slice = &battery[starting_point..=(battery_length - (12 - position))];

            let (idx, max_digit) = slice
                .char_indices()
                .rev() // pick the first appearance of the number, not the last
                .map(|(i, c)| (i, c.to_digit(10).unwrap()))
                .max_by_key(|&(_, d)| d)
                .unwrap();

            // add starting point to take into account the index in the full battery
            prev_max_index = idx + starting_point;
            battery_joltage = battery_joltage + &max_digit.to_string();
        }
        let battery_joltage: u64 = battery_joltage.parse().unwrap();
        result += battery_joltage;
    }

    result
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_two() {
        let input = "\
987654321111111
811111111111119
234234234234278
818181911112111";

        let result = 3121910778619;

        assert_eq!(part2(&input), result);
    }
}
