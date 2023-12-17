from functools import reduce
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    return puzzle_input.splitlines()


def part1(lines):
    parts = [list(map(int, line.split(':')[1].split())) for line in lines]
    races = list(zip(parts[0], parts[1]))

    ways_to_win = [
        sum(1 for elapsed_time in range(time) if (elapsed_time * (time - elapsed_time) > distance))
        for time, distance in races 
    ]

    return reduce(lambda x, y: x * y, ways_to_win)


def part2(lines):
    time = int(''.join(lines[0].split(':')[1].split()))
    distance = int(''.join(lines[1].split(':')[1].split()))

    # there must be a nicer way to do this than iterating through the ranges
    min_win = next(elapsed for elapsed in range(time) if elapsed * (time - elapsed) > distance)
    max_win = next(elapsed for elapsed in reversed(range(time)) if elapsed * (time - elapsed) > distance)

    return max_win - min_win + 1



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
