from functools import reduce
import operator
import pathlib
import sys
from icecream import ic

def parse(puzzle_input):
    scores_map = {}
    for line in puzzle_input.splitlines():
        parts = line.split(": ")
        game_id = int(parts[0].split()[1])
        scores = parts[1].split("; ")

        scores_map[game_id] = [
            {
                color_info.split()[1]: int(color_info.split()[0])
                for color_info in score.split(", ")
            }
            for score in scores
        ]

    return scores_map


def part1(data):
    max_scores = {"red": 12, "green": 13, "blue": 14}

    possible_games = [
        gameid
        for gameid, scores in data.items()
        if all(
            (score.get(color, 0) <= max_scores[color])
            for score in scores
            for color in max_scores
        )
    ]

    return sum(possible_games)


def part2(data):
    game_powers = [
        reduce(
            operator.mul,
            [
                max(score.get(color, 0) for score in scores)
                for color in ["red", "blue", "green"]
            ],
        )
        for scores in data.values()
    ]

    return sum(game_powers)


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
