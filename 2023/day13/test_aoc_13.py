import pathlib
import pytest
import aoc_13 as aoc

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
        [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
        ],
        [
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#",
        ],
    ]


def test_get_pairs():
    grid = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
    ]
    assert aoc.get_row_pairs(2, grid) == [
        ("##......#", "##......#"),
        ("..#.##.#.", "..#.##.#."),
        ("#.##..##.", "..##..##."),
    ]
    assert aoc.get_row_pairs(0, grid) == [("#.##..##.", "..#.##.#.")]
    assert aoc.get_row_pairs(5, grid) == [("..##..##.", "#.#.##.#.")]

    assert aoc.get_col_pairs(2, grid) == [
        ("##..###", "#....#."),
        ("..##...", ".#..#.#"),
        ("#.##..#", ".#..#.#"),
    ]
    assert aoc.get_col_pairs(0, grid) == [
        ('#.##..#', '..##...'),
    ]
    assert aoc.get_col_pairs(7, grid) == [
        ('##..###', '..##...'),
    ]



def test_part1_example1(example1):
    assert aoc.part1(example1) == 405


def test_part2_example1(example1):
    assert aoc.part2(example1) == 400
