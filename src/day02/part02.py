# Day 2
# Part 2

import re


def get_set_power(set):
    power = 1
    print(f"SET: {set}")
    for color in set:
        power *= set[color]

    return power


def extract_game_data(line):
    game_data = re.match(r'Game (\d+): ([^"]*)', line)
    game_num = game_data.group(1)
    rounds = game_data.group(2).split(";")

    return game_num, rounds


def get_min_set(game_data):
    min_set = {"red": 0, "green": 0, "blue": 0}

    for i, round in enumerate(game_data):
        print(f"Round: {i + 1}")
        cubes_selection = re.findall(r"(\d+) ([A-Za-z]+)", round)

        for selection in cubes_selection:
            print(selection)
            num_cubes = int(selection[0])
            color = selection[1]

            min_set[color] = max(min_set[color], num_cubes)

    return min_set


def display_sum_of_set_powers(fname):
    total = 0
    with open(fname) as f:
        for line in f:
            print("--------------------------")
            print()

            game_num, rounds = extract_game_data(line)

            print(f"GAME: {game_num}\n")

            fewest_num_cubes = get_min_set(rounds)
            print(fewest_num_cubes)

            total += get_set_power(fewest_num_cubes)

            print("--------------------------")

    print(total)


def main():
    # fname = "test_input.txt"
    fname = "input.txt"
    display_sum_of_set_powers(fname)


if __name__ == "__main__":
    main()
