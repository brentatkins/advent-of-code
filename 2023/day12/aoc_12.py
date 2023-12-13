from functools import reduce
import pathlib
import sys
from icecream import ic
import itertools as itertools


def parse(puzzle_input):
    return [
        (parts[0], list(map(int, parts[1].split(","))))
        for line in puzzle_input.splitlines()
        for parts in [line.split()]
    ]


def find_groups(value):
    groups = []
    count = 0
    for i, c in enumerate(value):
        if c == ".":
            continue
        if c == "#":
            if i == len(value) - 1 or value[i + 1] != "#":
                groups.append(count + 1)
                count = 0
            else:
                count += 1

    return groups


def generate_combinations(value):
    replacement_chars = (".", "#")
    count = value.count("?")
    replacements = itertools.product(replacement_chars, repeat=count)

    for replacement in replacements:
        iter_replacement = iter(replacement)
        replaced = "".join(c if c != "?" else next(iter_replacement) for c in value)
        yield replaced


def part1(lines):
    total = 0
    for record, real_groups in lines:
        valid = sum(1 for x in generate_combinations(record) if find_groups(x) == real_groups)
        total += valid
        ic(record, valid)

    return total


def part2(lines):
    total = 0
    for record, real_groups in lines:
        new_record = "?".join([record] * 5)
        new_groups = real_groups * 5

        # valid = sum(1 for x in generate_combinations(new_record) if find_groups(x) == new_groups)
        # total += valid
        # ic(record, valid, total)
        ic(record, new_record, real_groups,new_groups)
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
