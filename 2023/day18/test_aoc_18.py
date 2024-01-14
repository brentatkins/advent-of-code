import pathlib
import pytest
import aoc_18 as aoc

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
        ("R", 6, "#70c710"),
        ("D", 5, "#0dc571"),
        ("L", 2, "#5713f0"),
        ("D", 2, "#d2c081"),
        ("R", 2, "#59c680"),
        ("D", 2, "#411b91"),
        ("L", 5, "#8ceee2"),
        ("U", 2, "#caa173"),
        ("L", 1, "#1b58a2"),
        ("U", 2, "#caa171"),
        ("R", 2, "#7807d2"),
        ("U", 3, "#a77fa3"),
        ("L", 2, "#015232"),
        ("U", 2, "#7a21e3"),
    ]


def test_part1_example1(example1):
    assert aoc.part1(example1) == 62


def test_part2_example1(example1):
    assert aoc.part2(example1) == 952408144115
