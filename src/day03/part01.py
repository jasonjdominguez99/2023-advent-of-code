# Day 03
# Part 1

import re


def get_schematic_from_file(fname):
    schematic = []

    with open(fname) as f:
        for line in f:
            schematic.append(line.strip())

    # print(schematic)
    return schematic


def is_symbol(val):
    return val != "." and re.match(r"\d", val) == None


def is_missing(indices, row_num, schematic):
    # print(indices)

    if indices[0] > 0:
        j = indices[0] - 1
        val_to_check = schematic[row_num][j]
        if is_symbol(val_to_check):
            return False

        indices = [indices[0] - 1] + indices

    if indices[-1] < len(schematic[0]) - 1:
        j = indices[-1] + 1
        val_to_check = schematic[row_num][j]
        if is_symbol(val_to_check):
            return False

        indices = indices + [indices[-1] + 1]

    if row_num > 0:
        i = row_num - 1
        for j in indices:
            val_to_check = schematic[i][j]
            if is_symbol(val_to_check):
                return False

    if row_num < len(schematic) - 1:
        i = row_num + 1
        for j in indices:
            val_to_check = schematic[i][j]
            if is_symbol(val_to_check):
                return False

    return True


def get_part_numbers(schematic):
    part_nums = []

    for i, row in enumerate(schematic):
        # print(f"Row {i}")
        nums = re.finditer(r"(\d+)", row)
        for num in nums:
            num_idxs = [*range(num.span()[0], num.span()[1])]

            if not is_missing(num_idxs, i, schematic):
                part_num = int(num.group(0))
                part_nums.append(part_num)

    # print(part_nums)
    return part_nums


def display_sum_of_part_nums(part_nums):
    print(sum(part_nums))


def main():
    # fname = "test_input.txt"
    fname = "input.txt"

    engine = get_schematic_from_file(fname)
    part_nums = get_part_numbers(engine)

    display_sum_of_part_nums(part_nums)


if __name__ == "__main__":
    main()
