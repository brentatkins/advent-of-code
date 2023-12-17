import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    result = {'steps': {}}

    seeds, *blocks = puzzle_input.split("\n\n")
    result['seeds'] = [int(num) for num in seeds.split(':')[1].split()]
    
    for i, line in enumerate(blocks):
        _, *rows = line.splitlines()
        maps = [(int(x), int(y), int(z)) for row in rows for x, y, z in [row.split()]]
        result['steps'][i + 1] = maps
    
    return result

def get_seed_value(value, maps):
    for destination, source, length in maps:
        if (source <= value < source + length):
            return destination - source + value
    
    return value

def part1(data):
    lowest = None
    for seed in data['seeds']:
        seed_value = seed
        for step, maps in data['steps'].items():
            seed_value = get_seed_value(seed_value, maps)

        if lowest == None or lowest > seed_value:
            lowest = seed_value
            
    return lowest


def part2(data):
    seed_ranges = []
    for i in range(0, len(data['seeds']), 2):
        start = data['seeds'][i]
        length = data['seeds'][i + 1]
        seed_ranges.append((start, start + length))

    for maps in data['steps'].values():
        mapped_ranges = []
        while len(seed_ranges) > 0:
            seed_start, seed_end = seed_ranges.pop();

            for destination, source_start, length in maps:
                overlap_start = max(seed_start, source_start)
                overlap_end = min(seed_end, source_start + length)
                if overlap_start < overlap_end:
                    mapped_ranges.append((overlap_start - source_start + destination, overlap_end - source_start + destination))
                    if (overlap_start > seed_start):
                        seed_ranges.append((seed_start, overlap_start))
                    if (seed_end > overlap_end):
                        seed_ranges.append((seed_end, overlap_end))
                    break
            else:
                mapped_ranges.append((seed_start, seed_end))

        seed_ranges = mapped_ranges
    
    return min([s for (s, e) in seed_ranges])


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
