import pathlib
import pytest
import aoc_03 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_is_hit():
    assert aoc.is_hit(((2, 2), (2, 3)), ('*', (1,3))) == True
    assert aoc.is_hit(((0, 5), (0, 7)), ('*', (1,3))) == False

def test_parse_example1(example1):
    assert example1 == {
                            'numbers': [(467, ((0, 0), (0, 2))),
                                (114, ((0, 5), (0, 7))),
                                (35, ((2, 2), (2, 3))),
                                (633, ((2, 6), (2, 8))),
                                (617, ((4, 0), (4, 2))),
                                (58, ((5, 7), (5, 8))),
                                (592, ((6, 2), (6, 4))),
                                (755, ((7, 6), (7, 8))),
                                (664, ((9, 1), (9, 3))),
                                (598, ((9, 5), (9, 7)))],
                            'symbols':[('*', (1, 3)),
              ('#', (3, 6)),
              ('*', (4, 3)),
              ('+', (5, 5)),
              ('$', (8, 3)),
              ('*', (8, 5))]
                        }

def test_part1_example1(example1):
    assert aoc.part1(example1) == 4361

def test_part2_example1(example1):
    assert aoc.part2(example1) == 467835