from functools import reduce
import functools
from itertools import count
import pathlib
import sys
from icecream import ic
from enum import Enum
from collections import defaultdict


class Scores(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

card_rank_joker = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def parse(puzzle_input):
    lines = [
        (head, int(tail))
        for line in puzzle_input.splitlines()
        for head, tail in [line.split()]
    ]
    return lines


def score_hand(hand):
    counts = defaultdict(int)
    for card in hand:
        counts[card] += 1

    match sorted(counts.values(), reverse=True):
        case [5]:
            return Scores.FIVE_OF_A_KIND
        case [4, 1]:
            return Scores.FOUR_OF_A_KIND
        case [3, 2]:
            return Scores.FULL_HOUSE
        case [3, 1, 1]:
            return Scores.THREE_OF_A_KIND
        case [2, 2, 1]:
            return Scores.TWO_PAIR
        case [2, 1, 1, 1]:
            return Scores.ONE_PAIR
        case [1, 1, 1, 1, 1]:
            return Scores.HIGH_CARD
        case _:
            raise ValueError(hand)

def replace_jokers(hand):
    counts = defaultdict(int)
    for card in hand:
        counts[card] += 1

    if 0 < hand.count('J') < 5:
        max_card, _ = sorted(
            [x for x in counts.items() if x[0] != "J"],
            key=lambda item: item[1],
            reverse=True,
        )[0]
        hand = hand.replace("J", max_card)
    
    return hand


def part1(lines):
    ordered_hands = sorted(lines, key=lambda x: (score_hand(x[0]).value, [card_rank[card] for card in x[0]]))
    total = sum((i + 1) * score for i, (_, score) in enumerate(ordered_hands))
    return total


def part2(lines):
    ordered_hands = sorted(lines, key=lambda x: (score_hand(replace_jokers(x[0])).value, [card_rank_joker[card] for card in x[0]]))
    total = sum([(i + 1) * score for i, (_, score) in enumerate(ordered_hands)])
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
