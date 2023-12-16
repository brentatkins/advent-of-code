import pathlib
import pytest
import aoc_12 as aoc

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
        ("???.###", [1, 1, 3]),
        (".??..??...?##.", [1, 1, 3]),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6]),
        ("????.#...#...", [4, 1, 1]),
        ("????.######..#####.", [1, 6, 5]),
        ("?###????????", [3, 2, 1]),
    ]

def test_find_groups():
    assert aoc.find_groups('#.#.###') == [1, 1, 3]
    assert aoc.find_groups('####.#...#...') == [4,1,1]


def test_part1_example1(example1):
    assert aoc.part1(example1) == 21


def test_part2_example1(example1):
    assert aoc.part2(example1) == 525152