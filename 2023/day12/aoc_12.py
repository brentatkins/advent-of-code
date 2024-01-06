from functools import cache
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


def parse2(puzzle_input):
    return [
        (
            "?".join(parts[0] for _ in range(5)),
            [x for _ in range(5) for x in map(int, parts[1].split(","))],
        )
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


@cache
def count_combos(springs, groups):
    if not groups:
        return 1 if "#" not in springs else 0

    if not springs:
        return 0

    next_spring = springs[0]
    next_group = groups[0]

    if next_spring == ".":
        return count_combos(springs[1:], groups)

    if next_spring == "?":
        return count_combos("#" + springs[1:], groups) + count_combos(
            "." + springs[1:], groups
        )

    if next_spring == "#":
        if not groups:
            return 0

        this_batch = "".join(["#" if ch == "?" else ch for ch in springs[:next_group]])
        if this_batch != next_group * "#":
            return 0

        if len(springs) == next_group:
            return 1 if len(groups) == 1 else 0

        if springs[next_group] in ".?":
            return count_combos(springs[next_group + 1 :], groups[1:])

        return 0


def part1(lines):
    # total = 0
    # for record, real_groups in lines:
    #     valid = sum(
    #         1 for x in generate_combinations(record) if find_groups(x) == real_groups
    #     )
    #     total += valid
    #     ic(record, valid)

    # return total
    total = sum(count_combos(springs, tuple(groups)) for springs, groups in lines)
    return total


def part2(lines):
    total = sum(count_combos(springs, tuple(groups)) for springs, groups in lines)
    return total


def solve(puzzle_input):
    """Solve both parts and print the results."""
    solution1 = part1(parse(puzzle_input))
    solution2 = part2(parse2(puzzle_input))

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
