from functools import reduce
import pathlib
import sys
from icecream import ic
import pandas as pd

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


def print_grid(grid):
    df = pd.DataFrame(grid)
    ic(df)


def parse(puzzle_input):
    return puzzle_input.splitlines()


def expand_universe(grid):
    rows_to_add = [r for r, row in enumerate(grid) if all(c == "." for c in row)]
    new_row = "".join("." for _ in range(len(grid[0])))
    for i, r in enumerate(rows_to_add):
        grid.insert(r + i, new_row)

    cols_to_add = [
        i
        for i in range(len(grid[0]))
        if all(grid[r][i] == "." for r in range(len(grid)))
    ]
    for i, c in enumerate(cols_to_add):
        for r in range(len(grid)):
            grid[r] = grid[r][: c + i] + "." + grid[r][c + i :]

    return grid


# totally didn't have to do a BFS, could just walk the grid, there are no obstacles
def map_galaxy(start, grid):
    q = [(start, 0)]
    visited = [["." for _ in line] for line in grid]
    visited[start[0]][start[1]] = 0

    while q:
        ((r, c), count), *q = q
        nodes_to_add = []
        if r > 0 and visited[r - 1][c] == ".":
            nodes_to_add.append((r - 1, c))

        if r < len(grid) - 1 and visited[r + 1][c] == ".":
            nodes_to_add.append((r + 1, c))

        if c > 0 and visited[r][c - 1] == ".":
            nodes_to_add.append((r, c - 1))

        if c < len(grid[0]) - 1 and visited[r][c + 1] == ".":
            nodes_to_add.append((r, c + 1))

        for r2, c2 in nodes_to_add:
            q.append(((r2, c2), count + 1))
            if visited[r2][c2] == ".":
                visited[r2][c2] = count + 1

    return visited


def part1(lines):
    grid = expand_universe(lines)
    galaxies = [
        (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "#"
    ]

    paths_to_calc = {
        galaxy: [galaxies[j] for j in range(i + 1, len(galaxies))]
        for i, galaxy in enumerate(galaxies)
    }

    total = 0
    for galaxy, paths in paths_to_calc.items():
        mapped = map_galaxy(galaxy, grid)
        for path in paths:
            total += mapped[path[0]][path[1]]

    return total


def part2(grid):
    empty_rows = [r for r, row in enumerate(grid) if all(c == "." for c in row)]
    empty_cols = [
        i
        for i in range(len(grid[0]))
        if all(grid[r][i] == "." for r in range(len(grid)))
    ]

    galaxies = [
        (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "#"
    ]

    total = 0
    expander = 1000000

    paths_to_calc = {
        galaxy: [galaxies[j] for j in range(i + 1, len(galaxies))]
        for i, galaxy in enumerate(galaxies)
    }

    for galaxy, paths in paths_to_calc.items():
        for path in paths:
            for r in range(min(galaxy[0], path[0]), max(galaxy[0], path[0])):
                if r in empty_rows:
                    total += expander
                else:
                    total += 1
            for c in range(min(galaxy[1], path[1]), max(galaxy[1], path[1])):
                if c in empty_cols:
                    total += expander 
                else: 
                    total += 1


    return total


def solve(puzzle_input):
    """Solve both parts and print the results."""
    data = parse(puzzle_input)
    solution1 = 1 #part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
