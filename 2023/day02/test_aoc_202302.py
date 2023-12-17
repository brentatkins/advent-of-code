import pathlib
import pytest
import aoc_202302 as aoc

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
    assert example1 == {1: [{'blue': 3, 'red': 4}, {'blue': 6, 'green': 2, 'red': 1}, {'green': 2}],
                2: [{'blue': 1, 'green': 2},
                    {'blue': 4, 'green': 3, 'red': 1},
                    {'blue': 1, 'green': 1}],
                3: [{'blue': 6, 'green': 8, 'red': 20},
                    {'blue': 5, 'green': 13, 'red': 4},
                    {'green': 5, 'red': 1}],
                4: [{'blue': 6, 'green': 1, 'red': 3},
                    {'green': 3, 'red': 6},
                    {'blue': 15, 'green': 3, 'red': 14}],
                5: [{'blue': 1, 'green': 3, 'red': 6}, {'blue': 2, 'green': 2, 'red': 1}]}


def test_part1_example1(example1):
    assert aoc.part1(example1) == 8

def test_part1_example2(example1):
    assert aoc.part2(example1) == 2286
