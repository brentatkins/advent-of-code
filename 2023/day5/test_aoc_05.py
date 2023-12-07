import pathlib
import pytest
import aoc_05 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    assert example1 == {
        "seeds": [79, 14, 55, 13],
        "steps": {
            1: [(50, 98, 2), (52, 50, 48)],
            2: [(0, 15, 37), (37, 52, 2), (39, 0, 15)],
            3: [
                (49, 53, 8),
                (0, 11, 42),
                (42, 0, 7),
                (57, 7, 4),
            ],
            4: [(88, 18, 7), (18, 25, 70)],
            5: [(45, 77, 23), (81, 45, 19), (68, 64, 13)],
            6: [(0, 69, 1), (1, 0, 69)],
            7: [(60, 56, 37), (56, 93, 4)],
        },
    }

def test_get_seed_value():
    assert aoc.get_seed_value(79, [(50, 98, 2), (52, 50, 48)]) == 81
    assert aoc.get_seed_value(97, [(50, 98, 2), (52, 50, 48)]) == 99
    assert aoc.get_seed_value(1, [(50, 98, 2), (52, 50, 48)]) == 1
    assert aoc.get_seed_value(0, [(50, 98, 2), (52, 50, 48)]) == 0
    assert aoc.get_seed_value(50, [(50, 98, 2), (52, 50, 48)]) == 52
    assert aoc.get_seed_value(98, [(50, 98, 2), (52, 50, 48)]) == 50

# def test_get_seed_value():
#     # assert aoc.get_seed_range((79, 93), [(50, 98, 2), (52, 50, 48)]) == [(81, 95)]
#     assert aoc.get_seed_range((81, 95), [(88, 18, 7), (18, 25, 70)]) == [(74, 87), (95, 95)]
#     # assert aoc.get_seed_range((74, 87), [(45, 77, 23), (81, 45, 19), (68, 64, 13)]) == [(45, 55), (78, 80)]


def test_part1_example1(example1):
    assert aoc.part1(example1) == 35


def test_part2_example1(example1):
    assert aoc.part2(example1) == 46
