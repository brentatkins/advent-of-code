from functools import reduce
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    return puzzle_input.splitlines()


def tilt_line(current_line, line_below):
    result1 = ''
    result2 = ''
    for i, c in enumerate(current_line):
        if c == '.' and line_below[i] == 'O':
            result1 += 'O'
            result2 += '.'
            continue
        result1 += c
        result2 += line_below[i]

    return (result1, result2)


def part1(lines):
    for i in range(50):
        for i, line in enumerate(lines):
            if i == len(lines) - 1:
                lines[i] = ''.join('.' if c == 'O' and lines[i - 1][j] == '.' else c for j, c in enumerate(line))
            else:
                c, n = tilt_line(line, lines[i + 1])
                lines[i] = c
                lines[i + 1] = n

    total = sum(x.count('O') * (i + 1)  for i, x in enumerate(reversed(lines)))
    return total

def rotate_90(grid):
    return [list(reversed(x)) for x in zip(*grid)]

def part2(lines):
    # ic(lines)
    # ic([''.join(x) for x in rotate_90(lines)])

    cycles = 1000000000
    for cycle in range(cycles):
        # if cycle % 1000 == 0:
        # ic(cycle)
        for _ in range(4):
            for i in range(50):
                for i, line in enumerate(lines):
                    if i == len(lines) - 1:
                        lines[i] = ''.join('.' if c == 'O' and lines[i - 1][j] == '.' else c for j, c in enumerate(line))
                    else:
                        c, n = tilt_line(line, lines[i + 1])
                        lines[i] = c
                        lines[i + 1] = n
            lines = [''.join(x) for x in rotate_90(lines)]
    
    ic(lines)
    total = sum(x.count('O') * (i + 1)  for i, x in enumerate(reversed(lines)))
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
