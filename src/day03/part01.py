# Day 03
# Part 1

import re


def get_schematic_from_file(fname):
    schematic = []

    with open(fname) as f:
        for line in f:
            # schematic.append(
            #     [char for char in line.strip()]
            # )
            schematic.append(line.strip())

    print(schematic)
    return schematic


def get_missing_part_numbers(schematic):
    missing_part_nums = []

    # TODO

    return missing_part_nums


def display_sum_of_missing_part_nums(missing_part_nums):
    print(sum(missing_part_nums))


def main():
    fname = "test_input.txt"
    # fname = "input.txt"

    engine = get_schematic_from_file(fname)
    missing_part_nums = get_missing_part_numbers(engine)

    display_sum_of_missing_part_nums(missing_part_nums)


if __name__ == "__main__":
    main()
