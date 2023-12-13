from functools import reduce
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    patterns = puzzle_input.split("\n\n")
    return [pattern.splitlines() for pattern in patterns]


def get_diff(s1, s2):
    return [i for i, c1 in enumerate(s1) if c1 != s2[i]]


def get_row_pairs(r, grid):
    results = [(grid[r], grid[r + 1])]
    for i in range(1, len(grid)):
        if r - i >= 0 and r + 1 + i < len(grid):
            results.append((grid[r - i], grid[r + 1 + i]))

    return results


def get_col_pairs(c, grid):
    col1 = "".join(row[c] for row in grid)
    col2 = "".join(row[c + 1] for row in grid)
    results = [(col1, col2)]

    for i in range(1, len(grid[0])):
        if c - i >= 0 and c + 1 + i < len(grid[0]):
            comp1 = "".join(row[c - i] for row in grid)
            comp2 = "".join(row[c + 1 + i] for row in grid)
            results.append((comp1, comp2))

    return results


def find_mirror(pattern):
    result = 0
    for r in range(len(pattern) - 1):
        if pattern[r] == pattern[r + 1]:
            if all(r1 == r2 for r1, r2 in get_row_pairs(r, pattern)):
                result += (r + 1) * 100
                break

    for c in range(len(pattern[0]) - 1):
        col1 = [row[c] for row in pattern]
        col2 = [row[c + 1] for row in pattern]
        if col1 == col2:
            if all(c1 == c2 for c1, c2 in get_col_pairs(c, pattern)):
                result += c + 1
                break

    return result


def part1(patterns):
    total = sum([find_mirror(pattern) for pattern in patterns])
    return total


def part2(patterns):
    total = 0
    for pattern in patterns:
        for r in range(len(pattern) - 1):
            row_diffs = [get_diff(*pair) for pair in get_row_pairs(r, pattern)]
            if sum(len(diff) for diff in row_diffs) == 1:
                # we have a smudge
                total += (r + 1) * 100
                break

        for c in range(len(pattern[0]) - 1):
            col_diffs = [get_diff(*pair) for pair in get_col_pairs(c, pattern)]
            if sum(len(diff) for diff in col_diffs) == 1:
                # we have a smudge
                total += c + 1
                break

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
