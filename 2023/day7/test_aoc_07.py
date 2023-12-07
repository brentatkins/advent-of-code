import pathlib
import pytest
import aoc_07 as aoc

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
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]


def test_score_hand():
    assert aoc.score_hand('AAAAA') == aoc.Scores.FIVE_OF_A_KIND
    assert aoc.score_hand('AA8AA') == aoc.Scores.FOUR_OF_A_KIND
    assert aoc.score_hand('23332') == aoc.Scores.FULL_HOUSE
    assert aoc.score_hand('TTT98') == aoc.Scores.THREE_OF_A_KIND
    assert aoc.score_hand('23432') == aoc.Scores.TWO_PAIR
    assert aoc.score_hand('A23A4') == aoc.Scores.ONE_PAIR
    assert aoc.score_hand('23456') == aoc.Scores.HIGH_CARD





def test_part1_example1(example1):
    assert aoc.part1(example1) == 6440


def test_part2_example1(example1):
    assert aoc.part2(example1) == 5905
