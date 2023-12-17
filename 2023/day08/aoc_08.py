from functools import reduce
import itertools
import math
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    instruction, _, *raw_maps = puzzle_input.splitlines()
    maps = {}
    for map in raw_maps:
        key, parts = map.split(" = ")
        left, right = parts.replace("(", "").replace(")", "").split(", ")
        maps[key] = (left, right)
    return (instruction, maps)


def part1(lines):
    instruction, maps = lines
    node = "AAA"

    count = next(
        i
        for i, letter in enumerate(itertools.cycle(instruction), 1)
        if (node := maps[node][0] if letter == "L" else maps[node][1]) == "ZZZ"
    )
    return count


def part2(lines):
    instruction, maps = lines
    start_points = [key for key in maps.keys() if key[2] == "A"]

    counts = {}
    for point in start_points:
        node = point
        count = 0
        for letter in itertools.cycle(instruction):
            count += 1
            node = maps[node][0] if letter == "L" else maps[node][1]
            if node[2] == "Z":
                break
        counts[point] = count

    return math.lcm(*counts.values())


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
