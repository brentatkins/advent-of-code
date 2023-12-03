import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    lines = puzzle_input.splitlines()

    numbers = []
    symbols = []

    num = ""
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isnumeric():
                num = num + char
                if col == len(line) - 1 or not line[col + 1].isnumeric():
                    numbers.append(
                        (
                            int(num),
                            (
                                (row, col - len(num) + 1),
                                (row, col),
                            ),
                        ),
                    )
                    num = ""
            elif char != ".":
                symbols.append((char, (row, col)))

    return { 'numbers': numbers, 'symbols': symbols }


def is_hit(number_range, symbol):
    start, end = number_range
    hit_area_start = (start[0] - 1, start[1] - 1)
    hit_area_end = (end[0] + 1, end[1] + 1)

    return (
        hit_area_start[0] <= symbol[1][0] <= hit_area_end[0]
        and hit_area_start[1] <= symbol[1][1] <= hit_area_end[1]
    )


def part1(data):
    return sum(
        [
            num
            for (num, coord) in data['numbers']
            if any([is_hit(coord, symbol) for symbol in data['symbols']])
        ]
    )


def part2(data):
    total = 0
    for symbol in data['symbols']:
        hits = [num for (num, coord) in data['numbers'] if is_hit(coord, symbol)]
        if len(hits) == 2:
            total += hits[0] * hits[1]

    return total


def solve(puzzle_input):
    """Solve both parts and print the results."""
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
