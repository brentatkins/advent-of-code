from functools import reduce
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    return puzzle_input.split(',')

def calculate_hash(value):
    current_value = 0
    for c in value:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    
    return current_value

def part1(steps):
    total = sum([calculate_hash(step) for step in steps])
    return total


def part2(lines):
    return False



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
