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
    # df.to_excel('Day18_Output.xlsx')
    ic(df)


def parse(puzzle_input):
    return [
        (d, int(c), color[1:-1])
        for line in puzzle_input.splitlines()
        for d, c, color in [line.split()]
    ]


def part1(moves):

    grid = [["."]]
    r, c = 0, 0
    for direction, steps, _ in moves:

        if direction == "R":
            while c + 1 + steps > len(grid[0]):
                for row in grid:
                    row.append(".")
        if direction == "L":
            for _ in range(steps - c):
                c += 1
                for row in grid:
                    row.insert(0, ".")
        if direction == "D":
            while r + 1 + steps > len(grid):
                grid.append(["." for _ in range(len(grid[0]))])
        if direction == "U":
            for _ in range(steps - r):
                r += 1
                grid.insert(0, ["." for _ in range(len(grid[0]))])

        for _ in range(steps):
            if direction == "R":
                c += 1
            elif direction == "L":
                c -= 1
            elif direction == "D":
                r += 1
            elif direction == "U":
                r -= 1

            grid[r][c] = direction


    start_col = next(i for line in grid for i, ch in enumerate(line) if ch == 'R')
    q = [(1, start_col)]
    while q:
        r, c = q.pop()
        if grid[r][c] == '.':
            grid[r][c] = '#'
        
        neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for neighbour in neighbours:
            if grid[neighbour[0]][neighbour[1]] == '.':
                q.append(neighbour)


    # print_grid(grid)
    total = sum(0 if ch == "." else 1 for line in grid for ch in line)
    return total

def part2(moves):
    direction_map = {'0': 'R', '1': 'D', '2': 'L','3': 'U'}

    lines = []
    last_position = (0, 0)
    points = []
    trench_length = 0

    for _, _, move_code in moves:
        direction = direction_map[move_code[-1]]
        steps = int(move_code[1:-1], 16)
        trench_length += steps

        end_position = last_position
        match direction:
            case "R":
                end_position = (last_position[0], last_position[1] + steps)
                lines.append((direction, (last_position, end_position)))
            case "L":
                end_position = (last_position[0], last_position[1] - steps)
                lines.append((direction, (end_position, last_position)))
            case "D":
                end_position = (last_position[0] + steps, last_position[1])
                lines.append((direction, (last_position, end_position)))
            case "U":
                end_position = (last_position[0] - steps, last_position[1])
                lines.append((direction, (end_position, last_position)))

        points.append(end_position)
        last_position = end_position

    # 𝐾=12|(𝑥1𝑦2–𝑥2𝑦1)+(𝑥2𝑦3–𝑥3𝑦2)+(𝑥3𝑦4–𝑥4𝑦3)+(𝑥4𝑦1–𝑥1𝑦4)|.
    shoelace_area = 0
    for i, (y1, x1) in enumerate(points):
        (y2, x2) = points[i + 1] if i < (len(points) - 1) else points[0]
        shoelace_area += (x1 * y2) - (x2 * y1)
    
    shoelace_area = shoelace_area // 2

    picks_area = shoelace_area - trench_length // 2 + 1
    return picks_area + trench_length


    # # previous attempt
    ##############################
    # grid_rows_max, grid_rows_min = max(r for (_, (_, (r, _))) in lines), min(r for (_, (_, (r, _))) in lines)
    # grid_cols_max, grid_cols_min = max(c for (_, (_, (_r, c))) in lines), min(c for (_, (_, (_, c))) in lines)

    # vertical_lines = sorted([(d, line) for d, line in lines if d in ["U", "D"]], key=lambda x: x[1][0][1])

    # total = 0
    # for row in range(grid_rows_min, grid_rows_max):
    #     for col in range(grid_cols_min, grid_cols_max):

    #         match_up = None
    #         match_down = None
    #         for _, (v_start, v_end) in vertical_lines:
    #             if v_start[0] <= row <= v_end[0]:
    #                 if col >= v_start[1] and match_up == None:
    #                     match_up = (v_start, v_end)

    #                 if col <= v_start[1] and match_down == None:
    #                     match_down = (v_start, v_end)

    #         if match_up != None and match_down != None:
    #             total += 1

    # return total
    ########################


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
