import pathlib
import pytest
import aoc_06 as aoc

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
    assert example1 == ['Time:      7  15   30', 'Distance:  9  40  200']
    # [(7, 9), (15, 40), (30, 200)]


def test_part1_example1(example1):
    assert aoc.part1(example1) == 288


def test_part2_example1(example1):
    assert aoc.part2(example1) == 71503
