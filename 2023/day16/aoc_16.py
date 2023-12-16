from functools import reduce
import pathlib
import sys
from icecream import ic
from collections import deque
import pandas as pd

pd.set_option("display.max_rows", 5000)
pd.set_option("display.max_columns", 5000)
pd.set_option("display.width", 10000)


def print_grid(grid):
    df = pd.DataFrame(grid)
    ic(df)


UP = "⬆"
DOWN = "⬇"
LEFT = "⬅"
RIGHT = "➡"

directions = {UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1)}

direction_map = {
    ("|", LEFT): [UP, DOWN],
    ("|", RIGHT): [UP, DOWN],
    ("-", UP): [LEFT, RIGHT],
    ("-", DOWN): [LEFT, RIGHT],
    ("/", RIGHT): [UP],
    ("/", LEFT): [DOWN],
    ("/", DOWN): [LEFT],
    ("/", UP): [RIGHT],
    ("\\", RIGHT): [DOWN],
    ("\\", LEFT): [UP],
    ("\\", DOWN): [RIGHT],
    ("\\", UP): [LEFT],
}


def parse(puzzle_input):
    return puzzle_input.splitlines()


def count_energized(grid, start_position):
    q = deque()
    q.append(start_position)
    visited = [[[] for _ in line] for line in grid]

    while q:
        (r, c), direction = q.popleft()
        next_r, next_c = r + directions[direction][0], c + directions[direction][1]

        if (not 0 <= next_r < len(grid)) or (not 0 <= next_c < len(grid[0])):
            continue

        next_nodes = []

        if (
            grid[next_r][next_c] == "."
            or (grid[next_r][next_c] == "|" and direction in [UP, DOWN])
            or (grid[next_r][next_c] == "-" and direction in [LEFT, RIGHT])
        ):
            next_nodes.append(((next_r, next_c), direction))

        grid_char = grid[next_r][next_c]
        if (grid_char, direction) in direction_map:
            for new_direction in direction_map[(grid_char, direction)]:
                next_nodes.append(((next_r, next_c), new_direction))

        for (nr, nc), nd in next_nodes:
            if nd not in visited[nr][nc]:
                visited[nr][nc].append(nd)
                q.append(((nr, nc), nd))

    total = sum(1 if len(d) > 0 else 0 for line in visited for d in line)
    return total


def part1(grid):
    return count_energized(grid, ((0, -1), RIGHT))


def part2(grid):
    max_value = 0
    for r in range(len(grid)):
        max_value = max(max_value, count_energized(grid, ((r, 0), RIGHT)))
        max_value = max(max_value, count_energized(grid, ((r, len(grid[0]) - 1), LEFT)))
    for c in range(len(grid[0]) - 1):
        max_value = max(max_value, count_energized(grid, ((0, c), DOWN)))
        max_value = max(max_value, count_energized(grid, ((len(grid) - 1, c), UP)))

    return max_value


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
