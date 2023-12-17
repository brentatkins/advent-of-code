from functools import reduce
import pathlib
import sys


def parse(puzzle_input):
    return puzzle_input.splitlines()


def part1(data):
    linenumbers = []
    for line in data:
        numbers = list(filter(lambda c: c.isnumeric(), line))
        if numbers:
            linenumbers.append(int(numbers[0] + numbers[-1]))

    return sum(linenumbers)


def part2(data):
    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    linenumbers = []
    for line in data:
        numbers = []
        for i, c in enumerate(line):
            if c.isnumeric():
                numbers.append(c)
            else:
                numbers += [val for key, val in mapping.items() if line[i:].startswith(key)]

        linenumbers.append(int(numbers[0] + numbers[-1]))

    return sum(linenumbers)


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_data = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_data)
        print("\n".join(str(solution) for solution in solutions))
