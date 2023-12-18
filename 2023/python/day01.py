import regex as re
data = open("../data/day01.in").read().strip().split("\n")

def get_calibration_values(data: list[str]):
    cvalues = []
    for line in data:
        digits = [i for i in line if i.isdigit()]
        cvalues.append(int(digits[0] + digits[-1]))
    return cvalues

cvalues = get_calibration_values(data)
print("Part 1:", sum(cvalues)) # sol part 1

numbers_dict = {
    "eightwo" : 82,
    "eighthree" : 83,
    "twone" : 21,
    "nineight" : 98,
    "oneight" : 18,
    "one"   : 1,
    "two"   : 2,
    "three" : 3,
    "four"  : 4,
    "five"  : 5,
    "six"   : 6,
    "seven" : 7,
    "eight" : 8,
    "nine"  : 9
}

new_data = []
for line in data:
    tmp_line = line
    for number in numbers_dict:
        if number in line:
            tmp_line = tmp_line.replace(number, str(numbers_dict[number]))
    new_data.append(tmp_line)

real_cvalues = get_calibration_values(new_data)
print("Part 2:", sum(real_cvalues)) # sol part 2

# part 2 using regex

numbers_dict2 = {
    "one"   : 1,
    "two"   : 2,
    "three" : 3,
    "four"  : 4,
    "five"  : 5,
    "six"   : 6,
    "seven" : 7,
    "eight" : 8,
    "nine"  : 9
}

new_data2 = []
for line in data:
    nums = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
    tmp_nums = []
    for element in nums:
        tmp_element = element
        if element in numbers_dict2:
            tmp_element = str(numbers_dict2[element])
        tmp_nums.append(tmp_element)
    new_data2.append(tmp_nums)
sol = [int(numbers[0] + numbers[-1]) for numbers in new_data2]
print("Part 2 using regex:", sum(sol))