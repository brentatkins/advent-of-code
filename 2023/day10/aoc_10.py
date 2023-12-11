import pathlib
import sys
from icecream import ic
import pandas as pd


pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


def parse(puzzle_input):
    return puzzle_input.splitlines()


directions = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1],
]


def map_the_pipe(lines):
    start = next([i, line.index('S')] for i, line in enumerate(lines) if 'S' in line)

    q = [start]
    visited = [["." for _ in line] for line in lines]
    visited[start[0]][start[1]] = 0

    while len(q):
        (r, c), *q = q
        next_step = visited[r][c] + 1
        node_x = lines[r][c]

        nodes_to_add = []
        if r > 0 and node_x in "S|JL" and lines[r -1][c] in "|7F" and visited[r - 1][c] == '.':
            nodes_to_add.append((r - 1, c))
        if r < len(lines) - 1 and node_x in "S|7F" and lines[r + 1][c] in "|JL" and visited[r + 1][c] == '.':
            nodes_to_add.append((r + 1, c))
        if c > 0 and node_x in "S-J7" and lines[r][c - 1] in "-FL" and visited[r ][c - 1] == '.':
            nodes_to_add.append((r, c - 1))
        if c < len(lines[0]) - 1 and node_x in "S-FL" and lines[r][c + 1] in "-J7" and visited[r ][c + 1] == '.':
            nodes_to_add.append((r, c + 1))

        for r2, c2 in nodes_to_add:
            q.insert(0, (r2, c2))
            visited[r2][c2] = next_step

        # if next_step > 5:
        #     break

        # siblings = [
        #     (r + r_add, c + c_add)
        #     for r_add, c_add in directions
        #     if isvalid(
        #         r + r_add, c + c_add, lines, visited, (r_add, c_add), lines[r][c]
        #     )
        # ]

        # for next_r, next_c in siblings:
        #     q.insert(0, (next_r, next_c))
        #     visited[next_r][next_c] = next_step

    return visited


def part1(lines):
    grid = map_the_pipe(lines)
    total = len([1 for rows in grid for cell in rows if cell != "."])

    # df = pd.DataFrame(grid)
    # df.to_excel('Day10_Output.xlsx')
    # print(df)
    return total / 2


def isvalid(row, col, grid, visited, delta, source_node):
    if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
        return False
    if visited[row][col] != ".":
        return False
    node = grid[row][col]

    if node == ".":
        return False

    opposite_delta = {
        (0, 1): [0, -1],
        (0, -1): [0, 1],
        (1, 0): [-1, 0],
        (-1, 0): [1, 0],
    }

    if not can_move(node, opposite_delta[delta]):
        return False

    match delta:
        case (0, 1) if source_node in ["7", "J", "|"]:  # right
            return False
        case (0, -1) if source_node in ["F", "L", "|"]:  # left
            return False
        case (1, 0) if source_node in ["J", "L", "-"]:  # down
            return False
        case (-1, 0) if source_node in ["F", "7", "-"]:  # up
            return False
        case _:
            return True


def can_move(node, delta):
    # ic(node, delta)
    delta_map = {"right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0]}
    if node == "F" and delta in [delta_map["right"], delta_map["down"]]:
        return True
    if node == "7" and delta in [delta_map["left"], delta_map["down"]]:
        return True
    if node == "L" and delta in [delta_map["up"], delta_map["right"]]:
        return True
    if node == "J" and delta in [delta_map["up"], delta_map["left"]]:
        return True
    if node == "|" and delta in [delta_map["up"], delta_map["down"]]:
        return True
    if node == "-" and delta in [delta_map["left"], delta_map["right"]]:
        return True

    return False


def part2(lines):
    grid = map_the_pipe(lines)
    # new_grid purely for visualisation
    new_grid = [["." for _ in line] for line in lines] 
    count = 0
    for row_num, row in enumerate(grid):
        crossing_count = 0
        for col_num, val in enumerate(row):
            if val != ".":
                if row_num < len(lines) - 1 and grid[row_num + 1][col_num] != ".":
                    cell_below = grid[row_num + 1][col_num]
                    if cell_below - val == 1:
                        new_grid[row_num][col_num] = "⬇"
                        crossing_count += 1
                    if cell_below - val == -1:
                        new_grid[row_num][col_num] = "⬆"
                        crossing_count -= 1

            if val == "." and crossing_count != 0:
                count += 1
                new_grid[row_num][col_num] = "⭐️"

    df = pd.DataFrame(grid)
    ic(df)
    df2 = pd.DataFrame(new_grid)
    ic(df2)

    return count


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
