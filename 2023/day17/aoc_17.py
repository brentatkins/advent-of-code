from functools import reduce
import pathlib
import sys
from icecream import ic
from collections import deque
import pandas as pd
import heapq

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


def print_grid(grid):
    df = pd.DataFrame(grid)
    ic(df)


UP = "⬆"
DOWN = "⬇"
LEFT = "⬅"
RIGHT = "➡"

directions = {(-1, 0): UP, (1, 0): DOWN, (0, -1): LEFT, (0, 1): RIGHT}


def parse(puzzle_input):
    return [list(map(int, line)) for line in puzzle_input.splitlines()]


def get_direction(start, end):
    return (end[0] - start[0], end[1] - start[1])


def get_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        path.append(came_from[current])
        current = came_from[current]

    return list(reversed(path))


def cost(grid, node, look_forward=0, log=False):
    if look_forward == 0:
        return grid[node[0]][node[1]]

    costs = []
    for n, _ in get_neighbours(grid, node):
        costs.append(
            (
                n,
                grid[node[0]][node[1]] + cost(grid, n, look_forward - 1),
            )
        )

    if log:
        ic(node, costs)

    return min(c for _, c in costs)


def get_neighbours(grid, node):
    (r, c) = node
    result = []
    for (dr, dn), d in directions.items():
        (nr, nc) = (r + dr, c + dn)
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue

        result.append(((nr, nc), d))

    return result


def is_oppposite(d1, d2):
    if d1 == None or d2 == None:
        return False
    if (
        d1 + d2 == UP + DOWN
        or d1 + d2 == DOWN + UP
        or d1 + d2 == LEFT + RIGHT
        or d1 + d2 == RIGHT + LEFT
    ):
        return True

    return False


def part1(grid):
    q = []
    start = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    heapq.heappush(q, (0, (start, None, 0)))
    came_from = dict()
    cost_so_far = dict()

    came_from[(start, None, 0)] = None
    cost_so_far[(start, None, 0)] = 0

    goal_cell = None

    while q:
        c_cost, (current, d, d_count) = heapq.heappop(q)

        if current == goal:
            goal_cell = (current, d, d_count)
            break

        for next, nd in get_neighbours(grid, current):
            if is_oppposite(d, nd):
                continue

            if d == nd and d_count == 2:
                continue

            new_d_count = d_count + 1 if d == nd else 0

            new_cell_key = (next, nd, new_d_count)
            new_cost = c_cost + grid[next[0]][next[1]]

            if new_cell_key not in cost_so_far:
                cost_so_far[new_cell_key] = new_cost
                heapq.heappush(q, (new_cost, new_cell_key))
                came_from[new_cell_key] = (current, d, d_count)

    total = 0

    current = goal_cell
    path = [current[0]]
    while current != (start, None, 0):
        cell, _, _ = current
        total += grid[cell[0]][cell[1]]
        path.append(came_from[current][0])
        current = came_from[current]

    # path.pop()
    # for p in reversed(path):
    #     grid[p[0]][p[1]] = "*"

    # print_grid(grid)
    return total


def part2(grid):
    q = []
    start = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    heapq.heappush(q, (0, (start, None, 0)))
    came_from = dict()
    cost_so_far = dict()

    came_from[(start, None, 0)] = None
    cost_so_far[(start, None, 0)] = 0

    goal_cell = None

    while q:
        c_cost, (current, d, d_count) = heapq.heappop(q)

        if current == goal:
            goal_cell = (current, d, d_count)
            break

        for next, nd in get_neighbours(grid, current):
            if is_oppposite(d, nd):
                continue

            if d == nd and d_count == 9:
                continue

            new_d_count = d_count + 1 if d == nd else 0

            if current != start and d_count < 3 and new_d_count == 0:
                continue

            new_cost_key = (next, nd, new_d_count)
            new_cost = c_cost + grid[next[0]][next[1]]

            if new_cost_key not in cost_so_far:
                cost_so_far[new_cost_key] = new_cost
                heapq.heappush(q, (new_cost, (next, nd, new_d_count)))
                came_from[(next, nd, new_d_count)] = (current, d, d_count)

    total = 0

    current = goal_cell
    path = [current[0]]
    while current != (start, None, 0):
        cell, _, _ = current
        total += grid[cell[0]][cell[1]]
        path.append(came_from[current][0])
        current = came_from[current]

    # path.pop()
    # for p in reversed(path):
    #     grid[p[0]][p[1]] = "*"

    # print_grid(grid)
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
