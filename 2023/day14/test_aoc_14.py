import pathlib
import pytest
import aoc_14 as aoc

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
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]

def test_tilt_line():
    assert aoc.tilt_line('O....#....', 'O.OO#....#') == ('O.OO.#....', 'O...#....#')

def test_part1_example1(example1):
    assert aoc.part1(example1) == 136


def test_part2_example1(example1):
    assert aoc.part2(example1) == 64
