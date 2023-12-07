from itertools import count
from math import floor
import pathlib
import sys
from icecream import ic


def parse(puzzle_input):
    result = {}
    for line in puzzle_input.splitlines():
        card = int(line.split(':')[0].split()[1])
        numbers = line.split(': ')[1].split(' | ')
        winning_numbers, elf_numbers = [list(map(int, nums.split())) for nums in numbers]
        result[card] = (winning_numbers, elf_numbers)

    return result


def part1(data):
    matches = {}
    for (card, (winning_numbers, elf_numbers)) in data.items():
        matches[card] = 0
        for win in winning_numbers:
            for elf in elf_numbers:
                if (elf == win):
                    matches[card] += 1

    return sum([(2 ** (count - 1)) if count > 0 else 0 for count in matches.values()])


    

def part2(data):
    matches = {}
    for (card, (winning_numbers, elf_numbers)) in data.items():
        matches[card] = 0
        for win in winning_numbers:
            for elf in elf_numbers:
                if (elf == win):
                    matches[card] += 1

    cards = {}
    for card_number in range(1, len(matches) + 1):
        cards[card_number] = cards.get(card_number, 0) + 1

        score = matches[card_number]
        for i in range(card_number + 1, card_number + score + 1):
            cards[i] = cards.get(i, 0) + cards[card_number]


    return sum(cards.values())


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
