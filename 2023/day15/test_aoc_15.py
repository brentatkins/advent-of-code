import pathlib
import pytest
import aoc_15 as aoc

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
    assert example1 == [
        "rn=1",
        "cm-",
        "qp=3",
        "cm=2",
        "qp-",
        "pc=4",
        "ot=9",
        "ab=5",
        "pc-",
        "pc=6",
        "ot=7",
    ]


def test_calculate_hash():
    assert aoc.calculate_hash("HASH") == 52
    assert aoc.calculate_hash("rn=1") == 30

def test_part1_example1(example1):
    assert aoc.part1(example1) == 1320


def test_part2_example1(example1):
    assert aoc.part2(example1) == 145
