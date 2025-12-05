use std::ops::RangeInclusive;

fn main() {
    println!("part1!");
    let input = include_str!("day5.in");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> usize {
    let mut parts = input.splitn(2, "\n\n");
    let ingredient_ranges_ids = parts.next().unwrap();

    let mut candidate_ranges: Vec<RangeInclusive<usize>> = ingredient_ranges_ids
        .lines()
        .map(|line| {
            let (a, b) = line.split_once('-').unwrap();
            RangeInclusive::new(a.parse().unwrap(), b.parse().unwrap())
        })
        .collect();

    // sort the start of each interval
    candidate_ranges.sort_by_key(|range| *range.start());

    let mut merged_intervals: Vec<RangeInclusive<usize>> = Vec::new();
    merged_intervals.push(candidate_ranges.remove(0));

    for candidate_range in candidate_ranges {
        let last_added_range = merged_intervals.pop().unwrap();

        if candidate_range.end() < last_added_range.end() {
            // do nothing, it is fully include. we mvoe the range as is back to merged_intervals
            merged_intervals.push(last_added_range);
        } else if candidate_range.start() <= last_added_range.end()
            && last_added_range.end() < candidate_range.end()
        {
            // edit the last_added_range with a new end and push it
            merged_intervals.push(RangeInclusive::new(
                last_added_range.start().clone(),
                candidate_range.end().clone(),
            ));
        } else if candidate_range.start() > last_added_range.end() {
            // it is a completely new range to the right
            merged_intervals.push(last_added_range);
            merged_intervals.push(candidate_range);
        } else {
            merged_intervals.push(last_added_range);
        }
    }

    merged_intervals
        .iter()
        .map(|interval| *interval.end() - interval.start() + 1)
        .sum()
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_two() {
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

        let result = 14;

        assert_eq!(part2(&input), result);
    }
}
