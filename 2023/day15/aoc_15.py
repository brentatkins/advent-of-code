from functools import reduce
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    return puzzle_input.split(",")


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


def part2(steps):
    boxes = {}
    for step in steps:
        if step[-1] == "-":
            label = step[:-1]
            box = calculate_hash(label)
            if box in boxes.keys():
                boxes[box] = [(l, f) for l, f in boxes[box] if l != label]
        else:
            label = step[:-2]
            focal_length = int(step[-1])
            box = calculate_hash(label)
            if box in boxes.keys():
                if label in [l for l, f in boxes[box]]:
                    boxes[box] = [
                        (l, focal_length) if l == label else (l, f)
                        for l, f in boxes[box]
                    ]
                else:
                    boxes[box].append((label, focal_length))
            else:
                boxes[box] = [(label, focal_length)]

    total = 0
    for box, lenses in boxes.items():
        if len(lenses) > 0:
            for i, (_, focal_length) in enumerate(lenses):
                total += (box + 1) * (i + 1) * focal_length

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
