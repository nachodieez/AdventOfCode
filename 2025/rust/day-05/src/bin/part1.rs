use std::ops::RangeInclusive;

fn main() {
    println!("part1!");
    let input = include_str!("day5.in");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> usize {
    let mut parts = input.splitn(2, "\n\n");
    let ingredient_ranges_ids = parts.next().unwrap();
    let available_ingredient_ids = parts.next().unwrap();

    let ranges: Vec<RangeInclusive<usize>> = ingredient_ranges_ids
        .lines()
        .map(|line| {
            let (a, b) = line.split_once('-').unwrap();
            RangeInclusive::new(a.parse().unwrap(), b.parse().unwrap())
        })
        .collect();

    let ingredients: Vec<usize> = available_ingredient_ids
        .lines()
        .map(|line| line.parse().unwrap())
        .collect();

    let valid: Vec<usize> = ingredients
        .iter()
        .cloned()
        .filter(|ing| ranges.iter().any(|range| range.contains(ing)))
        .collect();

    valid.len()
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_one() {
        let input = "\
3-5
10-14
16-20
12-18

1
5
8
11
17
32";

        let result = 3;

        assert_eq!(part1(&input), result);
    }
}
