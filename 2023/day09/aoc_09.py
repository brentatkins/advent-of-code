from functools import reduce
from itertools import pairwise
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    result = [list(map(int, line.split())) for line in puzzle_input.splitlines()]
    return result

# foudn this implementation on the web and it's much neater than mine (see part 2)
def extrapolate(numbers):
    if list(set(numbers)) == [0]:
        return 0
    diffs = [b - a for a, b in pairwise(numbers)]
    return numbers[-1] + extrapolate(diffs)


def part1(lines):
    return sum(list(map(extrapolate, lines)))



def part2(lines):
    next_values = []
    for line in lines:
        transforms = [line]
        current = line
        
        while list(set(current)) != [0]:
            current = [b - a for a, b in pairwise(current)]
            transforms.append(current)

        extras = []
        for i in reversed(range(len(transforms))):
            if extras == []:
                extras.append(0)
                continue

            new_value = transforms[i][0] - extras[-1]
            extras.append(new_value)

        next_values.append(extras[-1])
    return sum(next_values)


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
