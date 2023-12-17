import pathlib
import pytest
import aoc_04 as aoc

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
        1: ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
        2: ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        3: ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
        4: ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
        5: ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
        6: ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]),
    }


def test_part1_example1(example1):
    assert aoc.part1(example1) == 13


def test_part2_example1(example1):
    assert aoc.part2(example1) == 30
