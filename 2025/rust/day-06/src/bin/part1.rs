use regex::Regex;

fn main() {
    println!("part1!");
    let input = include_str!("day6.in");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> u64 {
    let re_numbers = Regex::new(r"\d+").unwrap();
    let re_operators = Regex::new(r"[+*]").unwrap();

    let mut lines = input.lines();

    let operators_line = lines.next_back().unwrap();

    let numbers_lines: Vec<Vec<u64>> = lines
        .map(|line| {
            re_numbers
                .find_iter(line)
                .map(|number| number.as_str().parse().unwrap())
                .collect()
        })
        .collect();

    let operators: Vec<&str> = re_operators
        .find_iter(operators_line)
        .map(|operator| operator.as_str())
        .collect();

    assert_eq!(numbers_lines[0].len(), operators.len());

    let mut sol1 = 0;

    let first_line = &numbers_lines[0];
    let second_line = &numbers_lines[1];
    let third_line = &numbers_lines[2];

    // add fourth line for real input
    // let fourth_line = &numbers_lines[3];

    for operation_number in 0..operators.len() {
        let to_sum = match operators[operation_number] {
            "+" => {
                first_line[operation_number]
                    + second_line[operation_number]
                    + third_line[operation_number]
                //             + fourth_line[operation_number]
            }
            "*" => {
                first_line[operation_number]
                    * second_line[operation_number]
                    * third_line[operation_number]
                //           * fourth_line[operation_number]
            }
            _ => 0,
        };

        sol1 += to_sum;
    }

    sol1
}

#[cfg(test)]
mod test {
    use super::*; // go to the parent module

    #[test]
    fn example_part_one() {
        let input = "\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  ";

        let result = 4277556;

        assert_eq!(part1(&input), result);
    }
}
