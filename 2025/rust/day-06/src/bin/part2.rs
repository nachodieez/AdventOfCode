use regex::Regex;

fn main() {
    println!("part2!");
    let input = include_str!("day6.in");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> u64 {
    let re_numbers = Regex::new(r"\d+").unwrap();
    let re_operators = Regex::new(r"[+*]").unwrap();

    let mut lines = input.lines();

    let operators_line = lines.next_back().unwrap();

    let numbers_lines: Vec<Vec<&str>> = lines
        .map(|line| {
            re_numbers
                .find_iter(line)
                .map(|number| number.as_str())
                .collect()
        })
        .collect();

    let operators: Vec<&str> = re_operators
        .find_iter(operators_line)
        .map(|operator| operator.as_str())
        .collect();

    assert_eq!(numbers_lines[0].len(), operators.len());

    let mut max_number_sizes: Vec<usize> = vec![];

    // for each group, I want to find the biggest number
    for operation_number in 0..operators.len() {
        let mut max_number = 0;
        for line in &numbers_lines {
            max_number = max_number.max(line[operation_number].len());
        }
        max_number_sizes.push(max_number);
    }

    let lines: Vec<String> = input.lines().map(|line| line.to_string()).collect();

    let mut sol2 = 0;
    let mut pos = 0;
    for i in 0..max_number_sizes.len() {
        let operator = operators[i];
        let max_number_size = max_number_sizes[i];

        let mut nums: Vec<String> = vec![];
        for l in 0..(lines.len() - 1) {
            nums.push(lines[l][pos..(pos + max_number_size)].to_string());
        }

        // the final number of real nums for each operation is equal to the max number size
        let mut real_nums: Vec<u64> = vec![];

        // j is the pointer that moves along the number chars
        for j in 0..max_number_size {
            let mut vertical_number = "".to_string();
            // nums are already is order
            for num in &nums {
                let char: &str = &num.chars().nth(j).unwrap().to_string();
                if char != "" {
                    vertical_number = vertical_number + char;
                }
            }
            real_nums.push(vertical_number.trim().parse().unwrap());
        }

        sol2 += match operator {
            "+" => real_nums.iter().sum::<u64>(),
            "*" => real_nums.iter().product::<u64>(),
            _ => 0,
        };

        pos += max_number_size + 1;
    }

    sol2
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_two() {
        let input = "\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  ";

        let result = 3263827;

        assert_eq!(part2(&input), result);
    }
}
