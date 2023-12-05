# Day 1
# Part 1

import re


def main():
    # fname = "test_input.txt"
    fname = "input.txt"

    with open(fname) as file:
        total = 0
        for line in file:
            digits_in_line = re.findall(r"\d", line)
            calibration_val = digits_in_line[0] + digits_in_line[-1]
            total += int(calibration_val)

    print(total)


if __name__ == "__main__":
    main()
