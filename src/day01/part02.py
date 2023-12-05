# Day 1
# Part 2

import re


def to_int(digit):
    if digit == "one" or digit == "1":
        return 1
    elif digit == "two" or digit == "2":
        return 2
    elif digit == "three" or digit == "3":
        return 3
    elif digit == "four" or digit == "4":
        return 4
    elif digit == "five" or digit == "5":
        return 5
    elif digit == "six" or digit == "6":
        return 6
    elif digit == "seven" or digit == "7":
        return 7
    elif digit == "eight" or digit == "8":
        return 8
    elif digit == "nine" or digit == "9":
        return 9


def get_calibration_val(line):
    valid_digits = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    regex = "|".join(valid_digits) + r"|\d"
    digits_in_line = [to_int(digit) for digit in re.findall(rf"(?=({regex}))", line)]
    calibration_val = str(digits_in_line[0]) + str(digits_in_line[-1])

    return int(calibration_val)


def main():
    # fname = "test_input2.txt"
    fname = "input.txt"

    with open(fname) as file:
        total = 0
        for line in file:
            total += get_calibration_val(line)

    print(total)


if __name__ == "__main__":
    main()
