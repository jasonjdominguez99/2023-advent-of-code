# Day 2
# Part 1

import re


def num_ball_exceed_max(num_balls, color):
    RED_MAX = 12
    GREEN_MAX = 13
    BLUE_MAX = 14

    match color:
        case "red":
            return num_balls > RED_MAX
        case "green":
            return num_balls > GREEN_MAX
        case "blue":
            return num_balls > BLUE_MAX


def display_total_of_valid_game_ids(fname):
    total = 0
    with open(fname) as f:
        for line in f:
            print("--------------------------")
            print()

            valid_game = True

            game_data = re.match(r'Game (\d+): ([^"]*)', line)
            game_num = game_data.group(1)
            rounds = game_data.group(2).split(";")
            print(f"GAME: {game_num}\n")

            for i, round in enumerate(rounds):
                print(f"Round: {i + 1}")
                balls_selection = re.findall(r"(\d+) ([A-Za-z]+)", round)

                for selection in balls_selection:
                    print(selection)
                    num_balls = selection[0]
                    color = selection[1]

                    if num_ball_exceed_max(int(num_balls), color):
                        valid_game = False

            print(f"Valid Game: {valid_game}\n")
            if valid_game:
                total += int(game_num)

            print("--------------------------")

    print(total)


def main():
    # fname = "test_input.txt"
    fname = "input.txt"
    display_total_of_valid_game_ids(fname)


if __name__ == "__main__":
    main()
